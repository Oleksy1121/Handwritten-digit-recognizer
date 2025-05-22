import torch
from training.model_builder import TinyVGG
from training.image_transforms import simple_transform
from PIL import Image
import base64
import io
import os


class DigitPredictService:
    """
    Service for digit prediction using a training model.

    Handless loading the model, preprocesing images, running inference
    and formatting prediction results.

    """

    def __init__(self, model_path: str):
        """
        Initializes the digit prediction service by loading the model.

        Args:
            model_path (str): Path to the trained PyTorch model file.

        Raises:
            FileNotFoundError: If the model file does not exist at
                the specified path.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError("Check model weight path")

        self.model = TinyVGG(in_channels=1, hidden_units=10, out_features=10)
        self.model.load_state_dict(torch.load(model_path, weights_only=True))
        self.model.eval()

    def preprocessing_image(self, base64_string: str) -> Image.Image:
        """
        Decodes base64 image, conwerts to RGBA, and returns Alpha
        channel.

        Args:
            base64_string (str): Base64 encoded image string
                received from client.

        Raises:
            ValueError: If decoding the base64 string or
                opening/processing the image fails.

        Returns:
            Image.Image: The processed image (Alpha channel) as
                a PIL Image object.
        """

        try:
            img_bytes = base64.b64decode(base64_string)
            img = Image.open(io.BytesIO(img_bytes))
        except:
            raise ValueError("Error during encoding or opening image")

        img = img.convert("RGBA")
        _, _, _, alpha_channel = img.split()
        # alpha_channel.save('images/sample.png')
        return alpha_channel

    def format_pred_result(
        self, pred_probs: torch.Tensor, y_pred: torch.Tensor
    ) -> dict:
        """
        Formats prediction probability tensors into a dictionary.

        Args:
            pred_probs (torch.Tensor): Probability tensor output
                from the model (shape [1, 10]).
            y_pred (torch.Tensor): Predicted class index tensor
                output from the model (shape [1]).

        Returns:
            dict: A dictionary containing:
                "predictions": list[dict] - List of {"digit": int,
                    "probability": float, "isMax": bool} for each digit.
                "digit": int - The most probable digit.
                "coefficient": float - The confidence for the most probable digit.
        """

        results_list = []

        probs = pred_probs.squeeze().tolist()
        pred_digit = y_pred.item()

        for i, prob in enumerate(probs):
            results_list.append(
                {"digit": i, "probability": prob, "isMax": i == pred_digit}
            )

        return {
            "predictions": results_list,
            "digit": pred_digit,
            "coefficient": max(probs),
        }

    def predict(self, base64_string: str) -> dict:
        """
        Processes a base64 encoded image and predicts the digit
        using the loaded model.

        Orchestrates image preprocessing, tensor transformation,
        model inference, and result formatting.

        Args:
            base64_string (str): Base64 encoded image string.

        Returns:
            dict: A dictionary containing:
                "predictions": list[dict] - List of {"digit": int,
                    "probability": float, "isMax": bool} for each digit.
                "digit": int - The most probable digit.
                "coefficient": float - The confidence for the most probable digit.
        """

        img = self.preprocessing_image(base64_string)
        tensor = simple_transform(img).unsqueeze(dim=0)

        with torch.no_grad():
            pred_probs = torch.softmax(self.model(tensor), dim=1)
            y_pred = torch.argmax(pred_probs, dim=1)

        return self.format_pred_result(pred_probs, y_pred)
