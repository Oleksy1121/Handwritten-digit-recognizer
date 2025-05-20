import React, { useRef } from "react"
import {
    Button,
    ButtonContainer,
    DigitPredictiorContainer,
    Header,
} from "./styles"
import Canvas from "../CanvasDrawing"
import axios from '../../axios'

function DigitPredictor() {
    const canvasRef = useRef(null)

    const handleClearCanvas = () => {
      if (canvasRef.current) {
        canvasRef.current.clear()
      }
    }

    const getCanvasImage = () => {
      if (canvasRef.current) {
         return canvasRef.current.getImage()
      }
    }

    const getPrediction = async () => {
      const base64_string = getCanvasImage()
      console.log(base64_string)

      await axios.post('/predict', {'base64_string': base64_string})

    }

    return (
        <DigitPredictiorContainer>
            <Header>Draw your own digit !</Header>
            <Canvas ref={canvasRef}></Canvas>

            <ButtonContainer>
                <Button onClick={handleClearCanvas}>Clear</Button>
                <Button onClick={getPrediction}>Predict</Button>
            </ButtonContainer>

        </DigitPredictiorContainer>
    )
}

export default DigitPredictor
