import styled from 'styled-components'

export const DigitPredictiorContainer = styled.div`
    margin: 50px auto;
    padding: 20px;
    width: 800px;
    background: none;
    border: 1px solid black;
    border-radius: 20px;
    box-shadow: 0px 0px 30px black;

`

export const Header = styled.h1`
    text-align: center;
    color: white;
`

export const ButtonContainer = styled.div`
    margin: 50px auto;
    width: 80%;
    display: flex;
    justify-content: space-between;

    

`

export const Button = styled.button`
    width: 45%;
    height: 60px;
    font-size: 2.2em;
    font-weight: 500;
    background: none;
    border: 2px solid red;
    border-radius: 10px;
    color: red;
    cursor: pointer;

    transition: all 0.3s ease;

    &:hover{
        background: red;
        color: white;
        border: 2px solid gold;
    }
`