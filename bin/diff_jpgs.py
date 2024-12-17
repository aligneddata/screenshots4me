from PIL import Image
import sys
import os

#
# return 0 if files are about the same
# return 1 if files are significantly different
# unp if an error is found

def compare_images(image1_path, image2_path):
    try:
        # Open the images
        img1 = Image.open(image1_path).convert('RGB')
        img2 = Image.open(image2_path).convert('RGB')

        # Ensure dimensions match
        if img1.size != img2.size:
            raise ValueError("Images must have the same dimensions.")

        # Get pixel data
        pixels1 = list(img1.getdata())
        pixels2 = list(img2.getdata())

        # Calculate total pixels
        total_pixels = len(pixels1)

        # Count differing pixels
        differing_pixels = 0
        for i in range(total_pixels):
            # print("%d %d %d, %d %d %d" % (
            #     pixels1[i][0], pixels1[i][1], pixels1[i][2],
            #     pixels2[i][0], pixels2[i][1], pixels2[i][2],
            #     ))
            if not (pixels1[i][0] == pixels2[i][0]
                and pixels1[i][1] == pixels2[i][1]
                and pixels1[i][2] == pixels2[i][2]
                ):
                differing_pixels += 1
                # print("different")

        # Calculate percentage of differences
        difference_percentage = (1.0 * differing_pixels / total_pixels) * 100.0

        return difference_percentage

    except Exception as e:
        print(str(e))
        sys.exit(5)


if __name__ == "__main__":
    # Ensure script is called with two arguments for file paths
    if len(sys.argv) != 4:
        print("Usage: python compare_images.py <threshold> <image1.jpg> <image2.jpg>")
    else:
        THRESHOLD=int(sys.argv[1])
        image1 = sys.argv[2]
        image2 = sys.argv[3]

        # Check if files exist
        if not os.path.exists(image1):
            print(f"Error: File '{image1}' does not exist.")
            sys.exit(3)
        if not os.path.exists(image2):
            print(f"Error: File '{image2}' does not exist.")
            sys.exit(2)
        if not (THRESHOLD >= 0 and THRESHOLD <= 100):
            print("Abort: THRESHOLD should be 0-100.") 
            sys.exit(4)

        result = compare_images(image1, image2)
        if (os.getenv('DIFF_JPGS_DEBUG') == '1'):
            print("%.f Percentage of pixel differences" % result)
        if result <= THRESHOLD:
            sys.exit(0)  # about same
        else:
            sys.exit(1)  # different