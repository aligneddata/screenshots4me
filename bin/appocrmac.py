#
# purpose: parse a image file to txt/json/png(simplified)
#

# pip install ocrmac

import matplotlib.pyplot as plt
from ocrmac import ocrmac
import logging
import sys
import json

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
	encoding='utf-8',
	level=logging.WARNING)

def ocr_png_file(input_filename, output_txt_file, output_png_file, output_json_file):
	annotations = ocrmac.OCR(input_filename).recognize()
	# all_messages = []
	all_out_list = []
	outf = open(output_txt_file, "w")
	ojfile = open(output_json_file, "w")

	fig = plt.figure(figsize=(25,15))
	for annotation in annotations:
		# logging.info(annotation)

		x1 = annotation[2][0]
		y1 = annotation[2][1]
		message = annotation[0]
		confidence = annotation[1]

		logging.debug("Output: [%04d] [%s]" % (100*confidence, message))
		# all_messages.append(message)
		outf.write(message + "\n")
		plt.text(x1, y1, message, color='black', fontsize=12)

		out_dict = {}
		out_dict['x1'] = x1
		out_dict['y1'] = y1
		out_dict['message'] = message
		out_dict['confidence'] = confidence

		all_out_list.append(out_dict)

	plt.axis('off')
	plt.savefig(output_png_file)

	outf.close()
	all_out_dict = {}
	all_out_dict['all_out_json'] = all_out_list

	json_msg = json.dumps(all_out_dict, indent=4)
	ojfile.write(json_msg)
	logging.debug(json_msg)
	ojfile.close()
	return json.dumps(all_out_dict)


if __name__ == '__main__':
	input_filename = sys.argv[1]
	output_txt_file = sys.argv[2]
	output_png_file = sys.argv[3]
	output_json_file = sys.argv[4]

	logging.info("Start of program.")

	ocr_png_file(
		input_filename,
		output_txt_file,
		output_png_file,
		output_json_file)

	logging.info("End of program.")
	sys.exit(0)


