import styled from 'styled-components'


export const MainContainer = styled.div`
    display: flex;
    margin: 50px auto;
    border: 1px black solid;
    border-radius: 26px;
    width: 1200px;
    height: 900px;
    box-shadow: 0px 0px 30px black;
    overflow: hidden;
`


export const DigitPredictiorContainer = styled.div`
    padding: 20px;
    width: 800px;
    background: none;
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