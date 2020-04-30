#coding: utf-8
import pygame, random
import cv2, numpy as np, sys, pdb
from keras.models import load_model
import numpy as np
from collections import deque
import os

model = load_model('QuickDraw.h5')
def main():
   # background = pygame.image.load('image/background.png');
    emojis = get_QD_emojis()
    cv2.imshow("ANS",emojis[0])
    size = 560
    draw_on = False
    last_pos = (0, 0)
    color = (255, 255, 255)
    radius = 8
    screen = pygame.display.set_mode((size,size))
    try:
        pts = []
        stage = 0
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pts = roundline(screen, color, e.pos, last_pos,  radius)
                    firsttouch = True
                last_pos = e.pos
            if e.type == pygame.KEYDOWN:
        	    if e.key == ord('q'):
        		    screen.fill((0,0,0))
            data = pygame.image.tostring(screen, 'RGB')
            img = np.fromstring(data, np.uint8).reshape(size,size,3)
            #img = cv2.resize(img,(28,28)).astype(float)/127.5-1
            pred_probab, pred_class = keras_predict(model, img)
            if(pred_probab*100 < 50):
                cv2.imshow("ANS",emojis[10])
            else:
                cv2.imshow("ANS",emojis[pred_class])
            print(pred_class, pred_probab*100,"%")
            pygame.display.flip()

    except StopIteration:
        pass

def keras_predict(model, image):
    processed = keras_process_image(image)
    print("processed: " + str(processed.shape))
    pred_probab = model.predict(processed)[0]
    print(pred_probab);

    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class


def keras_process_image(img):
    image_x = 28
    image_y = 28
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, image_x, image_y, 1))
    return img


def get_QD_emojis():
    emojis_folder = 'qd_emo/'
    emojis = []
    for emoji in range(len(os.listdir(emojis_folder))):
        print(emoji)
        emojis.append(cv2.imread(emojis_folder + str(emoji) + '.png', -1))
    return emojis

def roundline(srf, color, start, end, radius=1):
    pygame.draw.line(srf, color, start, end, radius)
keras_predict(model, np.zeros((50, 50, 1), dtype=np.uint8))
if __name__ == '__main__':
    main()
