import React from "react"
import {
    PredictionBarContainer,
    PredictionLabel,
    ProgressBarFill,
    ProgressBarWrapper,
    ResultsContainer,
    ResultTextContainer,
    Text,
} from "./styles"

function Results( { results } ) {
    return (
        
        <ResultsContainer>
            {results.predictions?.map((pred) => (
            <PredictionBarContainer key={pred.digit}>
                <PredictionLabel>{pred.digit}</PredictionLabel>
                <ProgressBarWrapper>
                    <ProgressBarFill $probability={pred.probability}></ProgressBarFill>
                </ProgressBarWrapper>
            </PredictionBarContainer>
            ))}
            <ResultTextContainer>
            <Text>Your number is: <span>{ results.digit }</span></Text>
            </ResultTextContainer>
        </ResultsContainer>
    )
}

export default Results
