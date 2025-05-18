import React from 'react'
import { DigitPredictiorContainer, Header } from './styles'
import Canvas from '../CanvasDrawing'

function DigitPredictor() {
  return (
    <DigitPredictiorContainer>
      <Header>Draw your own digit !</Header>
      <Canvas></Canvas>
      
    </DigitPredictiorContainer>
  )
}

export default DigitPredictor
