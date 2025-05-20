import React, { useRef } from "react"
import {
    Button,
    ButtonContainer,
    DigitPredictiorContainer,
    Header,
} from "./styles"
import Canvas from "../CanvasDrawing"

function DigitPredictor() {
    const canvasRef = useRef(null)

    const handleClearCanvas = () => {
      if (canvasRef.current) {
        canvasRef.current.clear()
      }
    }

    const getCanvasImage = () => {
      if (canvasRef.current) {
        canvasRef.current.getImage()
      }
    }

    return (
        <DigitPredictiorContainer>
            <Header>Draw your own digit !</Header>
            <Canvas ref={canvasRef}></Canvas>

            <ButtonContainer>
                <Button onClick={handleClearCanvas}>Clear</Button>
                <Button onClick={getCanvasImage}>Predict</Button>
            </ButtonContainer>

        </DigitPredictiorContainer>
    )
}

export default DigitPredictor
