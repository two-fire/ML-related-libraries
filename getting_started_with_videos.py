import cv2

# 捕获变量
cap = cv2.VideoCapture(0)

# fourcc 四字节代码，指定视频编解码器
# (*'XVID') <-> ('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#20帧/s， size=640*480
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    # ret: true or false框架是否可用；
    # frame: 立即捕获或保存帧以显示此信息
    ret,frame = cap.read()
    if ret == True:
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # out 保存捕获
        out.write(frame)

        # 灰度处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        # 等待用户输入，q键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放捕获变量
cap.release()
out.release()
# 销毁所有窗口
cv2.destroyAllWindows()
