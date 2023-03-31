import os
import cv2
import logging
import pyvirtualcam

WIDTH = 1920
HEIGHT = 1080
FPS = 60
#LOG = logging.getLogger("webcamLogger")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))

def getCameras():
    err = 0
    index = 0
    msmf = []

    while err < 20:
        cap = cv2.VideoCapture(index)
        try:
            if cap.getBackendName()=="MSMF":
                msmf.append(index)
            elif cap.getBackendName()=="DSHOW":
                logging.debug("DSHOW: " + str(index))
            else:
                logging.debug("Unknown backend: " + str(cap.getBackendName()))
                logging.debug("Index: " + str(index))
        except:
            break
        cap.release()
        index += 1

    return msmf

def saveWebcams(msmf):
    for index in msmf:
        cap = cv2.VideoCapture(index)
        ret, img = cap.read()
        if ret:
            cv2.imwrite('Cam'+str(index)+'.png', img)
        else:
            logging.warn("Error reading MSMF camera: " + str(index))
        cap.release()

def getCamsWithNames():
    from pymf import get_MF_devices
    return get_MF_devices()
    

def getObsBotOpenCVID():
    cams = getCamsWithNames()
    for i, device_name in enumerate(cams):
        if device_name == "OBSBOT Tiny 4K Camera":
            return i

def getObsBotScreenshot(obsBotID=-1):
    if obsBotID == -1:
        obsBotID = getObsBotOpenCVID()
    cap = cv2.VideoCapture(obsBotID)
    ret, img = cap.read()

    if ret:
        cv2.imwrite('./images/OBS_Bot.png', img)
    else:
        logging.warn("Problem getting OBS Bot Screenshot: " + str(obsBotID))
    cap.release()
    return obsBotID

def doHistogram(frame):
    decke = cv2.imread('./images/Decke.png')
    spuele = cv2.imread('./images/Spuele.png')
    test = cv2.imread('./images/Test.png')

    histDecke = cv2.calcHist([decke], [0], None, [256], [0, 256])
    histSpuele = cv2.calcHist([spuele], [0], None, [256], [0, 256])
    histTest = cv2.calcHist([test], [0], None, [256], [0, 256])
    histOBSBot = cv2.calcHist([frame], [0], None, [256], [0, 256])

    testVsDeckeCorr = cv2.compareHist(histTest, histDecke, cv2.HISTCMP_CORREL)
    testVsSpueleCorr = cv2.compareHist(histTest, histSpuele, cv2.HISTCMP_CORREL)
    OBSBotVsDeckeCorr = cv2.compareHist(histOBSBot, histDecke, cv2.HISTCMP_CORREL)
    OBSBotVsSpueleCorr = cv2.compareHist(histOBSBot, histSpuele, cv2.HISTCMP_CORREL)

    testVsDeckeIntersect = cv2.compareHist(histTest, histDecke, cv2.HISTCMP_INTERSECT)
    testVsSpueleIntersect = cv2.compareHist(histTest, histSpuele, cv2.HISTCMP_INTERSECT)
    OBSBotVsDeckeIntersect = cv2.compareHist(histOBSBot, histDecke, cv2.HISTCMP_INTERSECT)
    OBSBotVsSpueleIntersect = cv2.compareHist(histOBSBot, histSpuele, cv2.HISTCMP_INTERSECT)

    logging.debug("----------------------------------------------------------")
    logging.debug("UNNORMALIZED")
    logging.debug("-----------------------------")
    logging.debug("testVsDeckeCorr: " + str(testVsDeckeCorr))
    logging.debug("OBSBotVsDeckeCorr: " + str(OBSBotVsDeckeCorr))
    logging.debug("-----------------------------")
    logging.debug("testVsSpueleCorr: " + str(testVsSpueleCorr))
    logging.debug("OBSBotVsSpueleCorr: " + str(OBSBotVsSpueleCorr))

    logging.debug("-----------------------------")
    logging.debug("-----------------------------")
    logging.debug("-----------------------------")
    logging.debug("testVsDeckeIntersect: " + str(testVsDeckeIntersect))
    logging.debug("OBSBotVsDeckeIntersect: " + str(OBSBotVsDeckeIntersect))
    logging.debug("-----------------------------")
    logging.debug("testVsSpueleIntersect: " + str(testVsSpueleIntersect))
    logging.debug("OBSBotVsSpueleIntersect: " + str(OBSBotVsSpueleIntersect))

    logging.debug("----------------------------------------------------------")

    if(OBSBotVsSpueleCorr > 0.51):
        logging.info("Correlation is higher than 0.51")

    if(OBSBotVsSpueleIntersect > 95000):
        logging.info("intersection is higher than 95000")


def startVirtualCam(obsBotID):
    cap = cv2.VideoCapture(obsBotID)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    trueWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    trueHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    trueFps = cap.get(cv2.CAP_PROP_FPS)

    with pyvirtualcam.Camera(width=trueWidth, height=trueHeight, fps=trueFps) as cam:
        logging.debug(f'Using virtual camera: {cam.device}')
        fpsCounter = 0
        while True:
            ret, frame = cap.read()

            if fpsCounter == 0:
                doHistogram(frame)
                fpsCounter = 0
            elif fpsCounter == trueFps*60:
                fpsCounter = 0

            cam.send(frame)
            cam.sleep_until_next_frame()
            fpsCounter += 1




obsBotID = getObsBotOpenCVID()
startVirtualCam(obsBotID)
