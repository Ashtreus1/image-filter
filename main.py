import cv2
import os

def apply_filter(image, filter_type):
	
	match(filter_type):
		case 'grayscale':
			return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		case 'blur':
			return cv2.GaussianBlur(image, (21, 21), 0)
		case 'edge':
			return cv2.Canny(image, 100, 500)
		case _:
			raise ValueError("Unknown filter type")

def main():
	
	image_dir = "images"
	
	image_name = input("Enter the name of your image file: ")
	
	image_path = os.path.join(image_dir, image_name)
	
	image = cv2.imread(image_path)
	
	
	if image is None:
		print("Could not open or find the file")
		return
		
	print("Choose a filter to apply:")
	print("[1] Grayscale")
	print("[2] Blur")
	print("[3] Edge Detection")
	
	choice = int(input("Enter the number of your choice: "))
	
	match(choice):
		case 1:
			filter_type = 'grayscale'
		case 2:
			filter_type = 'blur'
		case 3:
			filter_type = 'edge'
		case _:
			print("Invalid choice.")
			return
			
	filtered_image = apply_filter(image, filter_type)
	
	window_width = 500
	window_height = 500
	
	cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
	cv2.resizeWindow("Original Image", window_width, window_height)
	cv2.imshow("Original Image", image)
	
	cv2.namedWindow("Filtered Image", cv2.WINDOW_NORMAL)
	cv2.resizeWindow("Filtered Image", window_width, window_height)
	cv2.imshow("Filtered Image", filtered_image)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()


