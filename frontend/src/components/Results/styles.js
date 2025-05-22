import styled from "styled-components";


export const ResultsContainer = styled.div`
    display: flex;
    flex-direction: column;
    margin: auto;
    height: 100%; 
    flex-grow: 1; 
    
    justify-content: space-around;
    align-items: center;
    box-sizing: border-box;

    width: 280px;
    padding: 20px;
    border-left: 2px solid yellow;
    background: rgba(0, 0, 0, 0.3);
`;

export const PredictionBarContainer = styled.div`
    display:flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
`

export const PredictionLabel = styled.span`
    font-size: 2em; 
    font-weight: 600;
    margin-right: 15px;
    color: gold; 
    width: 25px; 
    text-align: right; 
`

export const ProgressBarWrapper = styled.div`
    display: flex;
    flex-grow: 1;
    height: 40px;
    border: 1px solid rgba(255, 215, 0, 0.8);;
    box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.5);
    border-radius: 15px;
    overflow: hidden;
`

export const ProgressBarFill = styled.div`
    background: linear-gradient(to right, #e74c3c, #f1c40f);
    height: 100%; 
    width: ${props => props.$probability * 100}%;
    border-radius: 0px;
    transition: width 0.5s ease-in-out; 
`

export const ResultTextContainer = styled.div`
    display: flex;
    align-items: baseline;

`

export const Text = styled.p`
    text-align: center;
    font-size: 2.1em;
    font-weight: 600;
    color: gold;

`

export const DigitText = styled(Text)`
    color:red;
    font-weight: 700;
    font-size: 3em;
    margin-left: 10px;
`