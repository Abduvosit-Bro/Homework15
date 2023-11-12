import time
import asyncio
import threading


# def red_light():
#     print("Красный")
#     time.sleep(1)
#
#
# def yellow_light():
#     print("Желтый")
#     time.sleep(1)
#
#
# def green_light():
#     print("Зеленый")
#     time.sleep(1)
#
#
# red_light()
# yellow_light()
# green_light()


# async def red_light():
#     print("Красный")
#     await asyncio.sleep(1)
#
#
# async def yellow_light():
#     print("Желтый")
#     await asyncio.sleep(1)
#
#
# async def green_light():
#     print("Зеленый")
#     await asyncio.sleep(1)
#
#
# async def main():
#     await red_light()
#     await yellow_light()
#     await green_light()
#
#
# asyncio.run(main())


def red_light():
    print("Красный")
    time.sleep(1)


def yellow_light():
    print("Желтый")
    time.sleep(1)


def green_light():
    print("Зеленый")
    time.sleep(1)


red_thread = threading.Thread(target=red_light)
yellow_thread = threading.Thread(target=yellow_light)
green_thread = threading.Thread(target=green_light)

red_thread.start()
yellow_thread.start()
green_thread.start()

red_thread.join()
yellow_thread.join()
green_thread.join()
