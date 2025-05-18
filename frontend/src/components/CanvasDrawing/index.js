import React, { useEffect, useRef, useState } from 'react'
import { CanvasContainer } from './styles'

function Canvas() {

    const canvasRef = useRef(null)
    const contextRef = useRef(null)
    const [isDrawing, setIsDrawing] = useState(false)

    useEffect(() => {   
        const canvas = canvasRef.current
        const displayWidth = canvas.clientWidth
        const displayHeight = canvas.clientHeight

        canvas.width = displayWidth 
        canvas.height = displayHeight 

        const context = canvas.getContext("2d")
        context.lineCap = "round"
        context.strokeStyle = "red"
        context.lineWidth = 5
        contextRef.current = context
    }, [])


    const startDrawing = ( {nativeEvent} ) => {

        const {offsetX, offsetY} = nativeEvent
        contextRef.current.beginPath()
        contextRef.current.moveTo(offsetX, offsetY)
        setIsDrawing(true)
    }

    const finishDrawing = () => {
        contextRef.current.closePath()
        setIsDrawing(false)

    }

    const draw = ( {nativeEvent} ) => {
        if (!isDrawing) return null
        
        const {offsetX, offsetY} = nativeEvent
        contextRef.current.lineTo(offsetX, offsetY)
        contextRef.current.stroke()
    }

    const handleMouseLeave = () => {
        if(isDrawing) {
            finishDrawing()
        }
    }


  return (
    <CanvasContainer
        onMouseDown={startDrawing}
        onMouseUp={finishDrawing}
        onMouseMove={draw}
        onMouseLeave={handleMouseLeave}
        ref={canvasRef}

    ></CanvasContainer>
  )
}

export default Canvas
