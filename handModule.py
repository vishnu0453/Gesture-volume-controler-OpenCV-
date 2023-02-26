import cv2
import mediapipe as mp
import time 

class handDetector():

    def __init__(self,mode=False,maxHands=1,detectCon=0.8,trackCon=0.5):

        self.mode=mode
        self.maxHands=maxHands
        self.detectCon=detectCon
        self.trackCon=trackCon
        self.hands_module=mp.solutions.hands
        self.hands=self.hands_module.Hands(self.mode,self.maxHands,int(self.detectCon),self.trackCon)
        self.draw_hands=mp.solutions.drawing_utils

    def mark_handlms(self,img,draw=True):
        rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(rgb_img)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.draw_hands.draw_landmarks(img,handlms,self.hands_module.HAND_CONNECTIONS)

        return img

    def coordinates(self,img):
        h,w,c=img.shape
        coords_list=[]
        if self.results.multi_hand_landmarks:
            selected_hand=self.results.multi_hand_landmarks[0]

            for id,coords in enumerate(selected_hand.landmark):
                cx,cy=(int(coords.x*w)),(int(coords.y*h))
                coords_list.append([id,cx,cy])
        return coords_list

    def id_coords(self,coordinates_list,id):  
        return coordinates_list[id]         



def main():
    cap=cv2.VideoCapture(0)
    detector=handDetector()
    while(True):
        ret,img=cap.read()
        img=detector.mark_handlms(img,True)
        l=detector.coordinates(img)
        if(len(l)!=0):
            print(l[4])
            print(l[5])
        # if(len(l)!=0):
        #     id_coord=detector.id_coords(l,6)
        #     print(id_coord)

        cv2.imshow('Hand detector',img)
        if(cv2.waitKey(1) & 0xFF==27):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()










