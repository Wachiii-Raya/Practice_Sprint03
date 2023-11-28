from threading import Thread
import dearpygui.dearpygui as dpg
import serial 
import enum


class PackageDevive(enum.Enum):
	UNDIFINED = bytearray(b'\x00')
	POTENTIOMETER = bytearray(b'\x01')
	SERVO = bytearray(b'\x02')
	HEARTBEAT = bytearray(b'\x03')
	LED = bytearray(b'\x04')



class PackageFlag(enum.Enum):
	UNDEFINED = bytearray(b'\x00')
	READ = bytearray(b'\x01')
	WRITE = bytearray(b'\x02')



class PackageConverter:
	def __init__(self):
		pass
	
 
	def get_package_object_template(self):
		package_object = {
			"device": PackageDevive.UNDIFINED,
			"flag": PackageFlag.UNDEFINED,
			"payload" : bytearray(0)
		}
		return package_object
	
 
	def convert_package_object_to_package_bytes(self, package_object):
		package_bytes = package_object["device"].value + package_object["flag"].value + package_object["payload"]
		return package_bytes


	def convert_package_bytes_to_package_object(self, package_bytes):
		package_object = self.get_package_object_template()
		package_object["device"] = package_bytes[0]
		package_object["flag"] = package_bytes[1]
		package_object["payload"] = package_bytes[2:]
		return package_object


	def get_LED_object_template(self, num_leds = 3):
		led_object = {}
		for led_index in range(1, num_leds + 1):
			led_name = f"LED_{led_index}"
			led_object[led_name] = False
		return led_object


	def convert_LED_object_to_LED_byte(self, led_object):
		size = len(led_object)
		# 0b0000_0000: LSB -> MSB, 0b0000_0001 is LED_1, 0b0000_0010 is LED_2, 0b0000_0100 is LED_3
		led_byte = 0b0000_0000
		for i in range(size):
			if led_object["LED_" + str(i + 1)]:
				led_byte = led_byte | (0b0000_0001 << i)		# 0b0000_0001 << i is 0b0000_0001, 0b0000_0010, 0b0000_0100
		return bytearray([led_byte])


	def convert_LED_byte_to_LED_object(self, led_byte):
		led_object = self.get_LED_object_template()
		size = len(led_object)
		for i in range(size):
			if led_byte & (0b0000_0001 << i):
				led_object["LED_" + str(i + 1)] = True
		return led_object


	def get_flag_object_template(self):
		flag_object = {
			"flag_mode": PackageFlag.UNDEFINED
		}
		return flag_object


	def convert_flag_object_to_flag_byte(self, flag_object):
		flag_byte = flag_object["flag_mode"].value
		return flag_byte


	def convert_flag_byte_to_flag_object(self, flag_byte):
		flag_object = self.get_flag_object_template()
		flag_object["flag_mode"] = PackageFlag(flag_byte)
		return flag_object



class UiController:
	def __init__(self):

  



if __name__ == '__main__':
	# ---------------Test: LED function----------------#
	# PackageConverter = PackageConverter()
	# led_object = PackageConverter.get_LED_object_template(3)
	# led_object["LED_1"] = True
	# led_object["LED_3"] = True
	# print(led_object)
	# led_byte = PackageConverter.convert_LED_object_to_LED_byte(led_object)
	# print(led_byte)
	# ---------------Test: Flag Mode function----------------#
	# PackageConverter = PackageConverter()
	# flag_object = PackageConverter.get_flag_object_template()
	# flag_object["flag_mode"] = PackageFlag.READ
	# flag_byte = PackageConverter.convert_flag_object_to_flag_byte(flag_object)
	# print(flag_byte)
	# flag_object = PackageConverter.convert_flag_byte_to_flag_object(flag_byte)
	# print(flag_object)
	# ---------------Test: Package function----------------#
	PackageConverter = PackageConverter()
	package_object = PackageConverter.get_package_object_template()
	package_object["device"] = PackageDevive.LED
	package_object["flag"] = PackageFlag.WRITE
	led_object = PackageConverter.get_LED_object_template(3)
	led_object["LED_1"] = True
	led_object["LED_3"] = True
	package_object["payload"] = PackageConverter.convert_LED_object_to_LED_byte(led_object)
	print(package_object)
	package_bytes = PackageConverter.convert_package_object_to_package_bytes(package_object)
	print(package_bytes)