import torch
from training.model_builder import TinyVGG
from training.image_transforms import simple_transform
from PIL import Image
import base64
import io
import os


class DigitPredictService:
    def __init__(self, model_path: str):
        if not os.path.exists(model_path):
            raise FileNotFoundError("Check model weight path")

        self.model = TinyVGG(in_channels=1, hidden_units=10, out_features=10)
        self.model.load_state_dict(torch.load(model_path, weights_only=True))
        self.model.eval()

    def preprocessing_image(self, base64_string: str) -> Image.Image:
        try:
            img_bytes = base64.b64decode(base64_string)
            img = Image.open(io.BytesIO(img_bytes))
        except:
            raise ValueError("Error during encodind or opening image")

        img = img.convert("RGBA")
        _, _, _, alpha_channel = img.split()
        # alpha_channel.save('images/sample.png')
        return alpha_channel

    def format_pred_result(self, pred_probs: torch.Tensor, y_pred: torch.Tensor):

        digit_pred = {}
        for i, prob in enumerate(pred_probs.squeeze().tolist()):
            digit_pred[i] = {"prob_value": prob, "isMax": i == y_pred.item()}

        return digit_pred

    def predict(self, base64_string: str):

        img = self.preprocessing_image(base64_string)
        tensor = simple_transform(img).unsqueeze(dim=0)

        with torch.no_grad():
            pred_probs = torch.softmax(self.model(tensor), dim=1)
            y_pred = torch.argmax(pred_probs, dim=1)

        return self.format_pred_result(pred_probs, y_pred)
