from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.connection_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await manager.send_personal_message("👋 Connected to the server!", websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received: {data}")

            # Echo message back
            await manager.send_personal_message(f"Echo: {data}", websocket)

            # Optional: Broadcast message
            # await manager.broadcast(f"Broadcast: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"Client disconnected: {websocket.client}")
