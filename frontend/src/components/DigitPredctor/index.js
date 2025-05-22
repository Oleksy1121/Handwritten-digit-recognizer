import React, { useRef, useState } from "react"
import {
    Button,
    ButtonContainer,
    DigitPredictiorContainer,
    Header,
    MainContainer,
} from "./styles"
import Canvas from "../CanvasDrawing"
import axios from "../../axios"
import Results from "../Results"

function DigitPredictor() {
    const canvasRef = useRef(null)
    const [results, setResults] = useState([])

    const handleClearCanvas = () => {
        if (canvasRef.current) {
            canvasRef.current.clear()
            setResults([])
        }
    }

    const getCanvasImage = () => {
        if (canvasRef.current) {
            return canvasRef.current.getImage()
        }
    }

    const getPrediction = async () => {
        const base64_string = getCanvasImage()

        if (canvasRef.current.isEmpty()) {
            return null
        }

        try {
            const response = await axios.post("/predict", {
                base64_string: base64_string,
            })
            //console.log(response.data.predict)
            setResults(response.data.predict)
        } catch (err) {
            console.log(err.message)
        }
    }

    return (
        <MainContainer>
            <DigitPredictiorContainer>
                <Header>Draw your own digit !</Header>
                <Canvas ref={canvasRef}></Canvas>
                <ButtonContainer>
                    <Button onClick={handleClearCanvas}>Clear</Button>
                    <Button onClick={getPrediction}>Predict</Button>
                </ButtonContainer>
            </DigitPredictiorContainer>
            <Results results={results}></Results>
        </MainContainer>
    )
}

export default DigitPredictor
