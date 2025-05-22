import React from "react"
import {
    DigitText,
    PredictionBarContainer,
    PredictionLabel,
    ProgressBarFill,
    ProgressBarWrapper,
    ResultsContainer,
    ResultTextContainer,
    Text,
} from "./styles"

function Results({ results }) {
    let resultText = ""

    if (results.length === 0) {
        resultText = "Draw your digit and click Predict to see predictions"
    } else {
        resultText = "Your number is: "
    }

    return (
        <ResultsContainer>
            {results.predictions?.map((pred) => (
                <PredictionBarContainer key={pred.digit}>
                    <PredictionLabel>{pred.digit}</PredictionLabel>
                    <ProgressBarWrapper>
                        <ProgressBarFill
                            $probability={pred.probability}
                        ></ProgressBarFill>
                    </ProgressBarWrapper>
                </PredictionBarContainer>
            ))}
            <ResultTextContainer>
                <Text> {resultText} </Text>
                <DigitText>{results.digit}</DigitText>
            </ResultTextContainer>
        </ResultsContainer>
    )
}

export default Results
