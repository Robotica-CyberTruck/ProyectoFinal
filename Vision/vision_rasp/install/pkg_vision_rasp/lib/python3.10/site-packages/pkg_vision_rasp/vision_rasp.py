import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher(Node):

    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera_image', 5)
        self.timer_period = 0.001  # segundos
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.i = 0
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)  # Usar el primer dispositivo de cámara
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Ancho de la imagen
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Altura de la imagen
        #self.cap.set(cv2.CAP_PROP_FPS, 30)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warn('No se puede capturar la imagen de la cámara')
            return
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'camera_frame'
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    image_publisher = ImagePublisher()

    rclpy.spin(image_publisher)

    # Destruir el nodo explicitamente
    image_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
