import React, {
    forwardRef,
    useEffect,
    useImperativeHandle,
    useRef,
    useState,
} from "react"
import { CanvasContainer } from "./styles"

const Canvas = forwardRef((props, ref) => {
    const canvasElementRef = useRef(null)
    const contextRef = useRef(null)
    const [isDrawing, setIsDrawing] = useState(false)
    const emptyCanvasBase64 = useRef(null)

    useImperativeHandle(ref, () => ({
        clear: clearCanvas,
        getImage: getImageAsBase64,
        isEmpty: isCanvasEmpty,
    }))

    useEffect(() => {
        const canvas = canvasElementRef.current
        const displayWidth = canvas.clientWidth
        const displayHeight = canvas.clientHeight

        canvas.width = displayWidth
        canvas.height = displayHeight

        const context = canvas.getContext("2d")
        context.lineCap = "round"
        context.strokeStyle = "red"
        context.lineWidth = 15
        contextRef.current = context

        clearCanvas()
        emptyCanvasBase64.current = getImageAsBase64()
    }, [])

    const startDrawing = ({ nativeEvent }) => {
        const { offsetX, offsetY } = nativeEvent
        contextRef.current.beginPath()
        contextRef.current.moveTo(offsetX, offsetY)
        setIsDrawing(true)
    }

    const finishDrawing = () => {
        contextRef.current.closePath()
        setIsDrawing(false)
    }

    const draw = ({ nativeEvent }) => {
        if (!isDrawing) return null

        const { offsetX, offsetY } = nativeEvent
        contextRef.current.lineTo(offsetX, offsetY)
        contextRef.current.stroke()
    }

    const handleMouseLeave = () => {
        if (isDrawing) {
            finishDrawing()
        }
    }

    const clearCanvas = () => {
        const canvas = canvasElementRef.current
        const context = contextRef.current
        if (context && canvas) {
            context.clearRect(0, 0, canvas.width, canvas.height)
        }
    }

    const getImageAsBase64 = (type = "image/png", quality = 1) => {
        const canvas = canvasElementRef.current
        if (!canvas) {
            console.error("Canvas element not found.")
            return null
        }

        return canvas.toDataURL(type, quality)
    }

    const isCanvasEmpty = () => {
        const currentCanvasBase64 = getImageAsBase64()
        return currentCanvasBase64 === emptyCanvasBase64.current
    }

    return (
        <CanvasContainer
            onMouseDown={startDrawing}
            onMouseUp={finishDrawing}
            onMouseMove={draw}
            onMouseLeave={handleMouseLeave}
            ref={canvasElementRef}
        ></CanvasContainer>
    )
})

export default Canvas
