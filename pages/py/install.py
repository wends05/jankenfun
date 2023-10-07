import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
from helper import hand_state
import pygame
pygame.font.init()
# from flask import Flask, render_template

# Initialize pygame
pygame.init()

# Load a sound file
sound_file = "./Resources/BGM.mp3"

# Create a Sound object
sound = pygame.mixer.Sound('Resources/BGM.mp3')

# Play the sound
sound.play()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 5
stateResult = False
startGame = False
endgame = False
# [AI, Player]
scores_AI = 3

scores_Player = 3
scores = 0

lose = False
win = False

# SOUND EFFECTS
win_sfx = pygame.mixer.Sound("Resources/win.mp3")
lose_sfx = pygame.mixer.Sound("Resources/lose.mp3")
Tie_sfx = pygame.mixer.Sound("Resources/Boink.mp3")
Start_sfx = pygame.mixer.Sound("Resources/Start.mp3")

# Effects

while True:
    imgBG = cv2.imread("Resources/BGF.png")
    success, img = cap.read()

    if lose:
        imgBG = cv2.imread("Resources/LOSE.png")
        imgBG = cv2.resize(imgBG, (1366, 768), interpolation=cv2.INTER_AREA)
        cv2.imshow("BGcover", imgBG)

    elif win == True:
        imgBG = cv2.imread("Resources/Win.jpeg")
        imgBG = cv2.resize(imgBG, (1366, 768), interpolation=cv2.INTER_AREA)
        cv2.imshow("BGcover", imgBG)

    else:
        imgScaled = cv2.resize(img, (0, 0), None, 0.495, 0.495)
        imgScaled = imgScaled[:, 42:275]

        # Find Hands
        hands, img = detector.findHands(imgScaled)  # with draw

        if startGame:

            if stateResult is False:
                timer = time.time() - initialTime
                cv2.putText(imgBG, str(int(timer)), (575, 608), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
                pygame.init()

                if timer > 5:
                    stateResult = True
                    timer = 0

                    if hands:
                        hand = hands[0]
                        fingers = detector.fingersUp(hand)
                        playerMove = hand_state(fingers)

                        randomNumber = random.randint(1, 3)
                        imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                        imgBG = cvzone.overlayPNG(imgBG, imgAI, (173, 155))

                        # Player Wins
                        if (playerMove == 1 and randomNumber == 3) or \
                                (playerMove == 2 and randomNumber == 1) or \
                                (playerMove == 3 and randomNumber == 2):
                            scores_AI -= 1
                            # SOUND EFFECT IF PLAYER WIN
                            win_sfx.play()
                            # Game loop
                            imgScore = cv2.imread('Resources/6.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgScore, (460, 276))

                        # AI Wins
                        if (playerMove == 3 and randomNumber == 1) or \
                                (playerMove == 1 and randomNumber == 2) or \
                                (playerMove == 2 and randomNumber == 3):
                            scores_Player -= 1
                            # SOUND EFFECT IF PLAYER LOSE
                            lose_sfx.play()
                            # Game loop
                            imgScore = cv2.imread('Resources/4.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgScore, (460, 276))

                        # TIE
                        if (playerMove == 3 and randomNumber == 3) or \
                                (playerMove == 2 and randomNumber == 2) or \
                                (playerMove == 1 and randomNumber == 1):
                            scores_AI -= 0
                            imgScore = cv2.imread('Resources/5.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgScore, (460, 276))

                        if (playerMove == 3 and randomNumber == 3) or \
                                (playerMove == 2 and randomNumber == 2) or \
                                (playerMove == 1 and randomNumber == 1):
                            scores_Player -= 0
                            # SOUND EFFECT IF TIE
                            Tie_sfx.play()
                            imgScore = cv2.imread('Resources/5.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgScore, (460, 276))

                        else:
                            endgame = True

        if endgame == True:

            if scores_AI == 0:
                 win = True
                 lose = False

            if scores_Player == 0:
                 lose = True
                 win = False

        imgBG[162:400, 810:1043] = imgScaled

        if stateResult:
            imgBG = cvzone.overlayPNG(imgBG, imgAI, (173, 155))
            imgBG = cvzone.overlayPNG(imgBG, imgScore, (460, 276))

        cv2.putText(imgBG, str(scores_AI), (269, 569), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(scores_Player), (910, 569), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

        # cv2.imshow("Image", img)
        imgBG = cv2.resize(imgBG, (1366, 768), interpolation=cv2.INTER_AREA)
        cv2.imshow("JankenFun", imgBG)  # cv2.imshow("Scaled", imgScaled)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        Start_sfx.play()

    if key == ord('r'):
        stateResult = False
        startGame = False
        endgame = False
        # [AI, Player]
        scores_AI = 3
        scores_Player = 3
        scores = 0
        sound.stop()
        sound.play()
        lose = False
        win = False
    
    if key == ord('q'):
        cv2.destroyWindow("JankenFun")









