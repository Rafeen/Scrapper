import json
import urllib.request
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

my_json = """{
	"productsById": [{
		"2894832": {
			"id": 2894832,
			"brandId": 4317,
			"brandName": "ROBERT BARAKETT",
			"styleNumber": "36349",
			"colorCount": 9,
			"colorDefaultId": "dusty pink",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=3_107869103-16_107681496-10_102528150-18_102658338-5_104277685-5_107681505-4_107681424-9_102658409-3_107681503",
			"colorsById": {
				"beluga": {
					"id": "beluga",
					"label": "BELUGA",
					"spriteIndex": 1,
					"mediaIds": [
						"16_107681496",
						"15_107681675",
						"12_107681672"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "16_107681496"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"10_102528150",
						"9_12790169",
						"1_12925101"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_102528150"
				},
				"blue night": {
					"id": "blue night",
					"label": "BLUE NIGHT",
					"spriteIndex": 3,
					"mediaIds": [
						"18_102658338",
						"3_101012803",
						"5_101012885"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "18_102658338"
				},
				"dusty pink": {
					"id": "dusty pink",
					"label": "DUSTY PINK",
					"spriteIndex": 0,
					"mediaIds": [
						"3_107869103",
						"12_107868712",
						"0_107689660"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "3_107869103"
				},
				"iron": {
					"id": "iron",
					"label": "IRON",
					"spriteIndex": 4,
					"mediaIds": [
						"5_104277685",
						"17_102658417",
						"19_12927339"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_104277685"
				},
				"orion blue": {
					"id": "orion blue",
					"label": "ORION BLUE",
					"spriteIndex": 5,
					"mediaIds": [
						"5_107681505",
						"18_107681678",
						"14_107681674"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107681505"
				},
				"rust": {
					"id": "rust",
					"label": "RUST",
					"spriteIndex": 6,
					"mediaIds": [
						"4_107681424",
						"15_107681455",
						"12_107681452"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "4_107681424"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 7,
					"mediaIds": [
						"9_102658409",
						"8_102658408",
						"11_102658251"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "9_102658409"
				},
				"winter purple": {
					"id": "winter purple",
					"label": "WINTER PURPLE",
					"spriteIndex": 8,
					"mediaIds": [
						"3_107681503",
						"9_107681689",
						"7_107681687"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "3_107681503"
				}
			},
			"colorIds": [
				"dusty pink",
				"beluga",
				"black",
				"blue night",
				"iron",
				"orion blue",
				"rust",
				"white",
				"winter purple"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107689660": {
					"id": "0_107689660",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107689660.jpg"
				},
				"10_102528150": {
					"id": "10_102528150",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_102528150.jpg"
				},
				"11_102658251": {
					"id": "11_102658251",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_102658251.jpg"
				},
				"12_107681452": {
					"id": "12_107681452",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107681452.jpg"
				},
				"12_107681672": {
					"id": "12_107681672",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107681672.jpg"
				},
				"12_107868712": {
					"id": "12_107868712",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107868712.jpg"
				},
				"14_107681674": {
					"id": "14_107681674",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107681674.jpg"
				},
				"15_107681455": {
					"id": "15_107681455",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107681455.jpg"
				},
				"15_107681675": {
					"id": "15_107681675",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107681675.jpg"
				},
				"16_107681496": {
					"id": "16_107681496",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107681496.jpg"
				},
				"17_102658417": {
					"id": "17_102658417",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_102658417.jpg"
				},
				"18_102658338": {
					"id": "18_102658338",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102658338.jpg"
				},
				"18_107681678": {
					"id": "18_107681678",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107681678.jpg"
				},
				"19_12927339": {
					"id": "19_12927339",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_12927339.jpg"
				},
				"1_12925101": {
					"id": "1_12925101",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_12925101.jpg"
				},
				"3_101012803": {
					"id": "3_101012803",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101012803.jpg"
				},
				"3_107681503": {
					"id": "3_107681503",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107681503.jpg"
				},
				"3_107869103": {
					"id": "3_107869103",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107869103.jpg"
				},
				"4_107681424": {
					"id": "4_107681424",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107681424.jpg"
				},
				"5_101012885": {
					"id": "5_101012885",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_101012885.jpg"
				},
				"5_104277685": {
					"id": "5_104277685",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_104277685.jpg"
				},
				"5_107681505": {
					"id": "5_107681505",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107681505.jpg"
				},
				"7_107681687": {
					"id": "7_107681687",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107681687.jpg"
				},
				"8_102658408": {
					"id": "8_102658408",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_102658408.jpg"
				},
				"9_102658409": {
					"id": "9_102658409",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_102658409.jpg"
				},
				"9_107681689": {
					"id": "9_107681689",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107681689.jpg"
				},
				"9_12790169": {
					"id": "9_12790169",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_12790169.jpg"
				}
			},
			"name": "Robert Barakett Georgia Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/robert-barakett-georgia-crewneck-t-shirt/2894832",
			"reviewCount": 457,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"3135708": {
			"id": 3135708,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "328910",
			"colorCount": 5,
			"colorDefaultId": "pink",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_104800971-15_104797275-14_107466814-14_107466794-4_105358804",
			"colorsById": {
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 1,
					"mediaIds": [
						"15_104797275",
						"16_104797336",
						"12_104797372"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_104797275"
				},
				"blue hydrangea": {
					"id": "blue hydrangea",
					"label": "BLUE HYDRANGEA",
					"spriteIndex": 2,
					"mediaIds": [
						"14_107466814",
						"8_107466828",
						"1_107466821"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_107466814"
				},
				"lavender spray": {
					"id": "lavender spray",
					"label": "LAVENDER SPRAY",
					"spriteIndex": 3,
					"mediaIds": [
						"14_107466794",
						"16_107466816",
						"10_107466810"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "14_107466794"
				},
				"pink": {
					"id": "pink",
					"label": "PINK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_104800971",
						"16_104800976",
						"7_104801047"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "11_104800971"
				},
				"white brilliant": {
					"id": "white brilliant",
					"label": "WHITE BRILLIANT",
					"spriteIndex": 4,
					"mediaIds": [
						"4_105358804",
						"8_105358808",
						"15_105358055"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "4_105358804"
				}
			},
			"colorIds": [
				"pink",
				"blue",
				"blue hydrangea",
				"lavender spray",
				"white brilliant"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107466810": {
					"id": "10_107466810",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107466810.jpg"
				},
				"11_104800971": {
					"id": "11_104800971",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_104800971.jpg"
				},
				"12_104797372": {
					"id": "12_104797372",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_104797372.jpg"
				},
				"14_107466794": {
					"id": "14_107466794",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107466794.jpg"
				},
				"14_107466814": {
					"id": "14_107466814",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107466814.jpg"
				},
				"15_104797275": {
					"id": "15_104797275",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104797275.jpg"
				},
				"15_105358055": {
					"id": "15_105358055",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105358055.jpg"
				},
				"16_104797336": {
					"id": "16_104797336",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_104797336.jpg"
				},
				"16_104800976": {
					"id": "16_104800976",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_104800976.jpg"
				},
				"16_107466816": {
					"id": "16_107466816",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107466816.jpg"
				},
				"1_107466821": {
					"id": "1_107466821",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107466821.jpg"
				},
				"4_105358804": {
					"id": "4_105358804",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105358804.jpg"
				},
				"7_104801047": {
					"id": "7_104801047",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104801047.jpg"
				},
				"8_105358808": {
					"id": "8_105358808",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105358808.jpg"
				},
				"8_107466828": {
					"id": "8_107466828",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107466828.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Smartcare™ Trim Fit Solid Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-smartcare-trim-fit-solid-dress-shirt/3135708",
			"reviewCount": 186,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"3218760": {
			"id": 3218760,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "389526",
			"colorCount": 5,
			"colorDefaultId": "red maple",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_106797418-13_103843993-3_13350203-11_100278671-15_103843995",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"13_103843993",
						"14_103843994",
						"19_103843959"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_103843993"
				},
				"graphite": {
					"id": "graphite",
					"label": "GRAPHITE",
					"spriteIndex": 2,
					"mediaIds": [
						"3_13350203",
						"4_13350204",
						"5_13350205"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_13350203"
				},
				"ink blue": {
					"id": "ink blue",
					"label": "INK BLUE",
					"spriteIndex": 3,
					"mediaIds": [
						"11_100278671",
						"2_100279042",
						"16_100278756"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_100278671"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 4,
					"mediaIds": [
						"15_103843995",
						"6_10981646",
						"7_11060767"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_103843995"
				},
				"red maple": {
					"id": "red maple",
					"label": "RED MAPLE",
					"spriteIndex": 0,
					"mediaIds": [
						"18_106797418",
						"13_106193173",
						"13_106193233"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "18_106797418"
				}
			},
			"colorIds": [
				"red maple",
				"black",
				"graphite",
				"ink blue",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_100278671": {
					"id": "11_100278671",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_100278671.jpg"
				},
				"13_103843993": {
					"id": "13_103843993",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_103843993.jpg"
				},
				"13_106193173": {
					"id": "13_106193173",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106193173.jpg"
				},
				"13_106193233": {
					"id": "13_106193233",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106193233.jpg"
				},
				"14_103843994": {
					"id": "14_103843994",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103843994.jpg"
				},
				"15_103843995": {
					"id": "15_103843995",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_103843995.jpg"
				},
				"16_100278756": {
					"id": "16_100278756",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100278756.jpg"
				},
				"18_106797418": {
					"id": "18_106797418",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106797418.jpg"
				},
				"19_103843959": {
					"id": "19_103843959",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_103843959.jpg"
				},
				"2_100279042": {
					"id": "2_100279042",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_100279042.jpg"
				},
				"3_13350203": {
					"id": "3_13350203",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_13350203.jpg"
				},
				"4_13350204": {
					"id": "4_13350204",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_13350204.jpg"
				},
				"5_13350205": {
					"id": "5_13350205",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_13350205.jpg"
				},
				"6_10981646": {
					"id": "6_10981646",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_10981646.jpg"
				},
				"7_11060767": {
					"id": "7_11060767",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_11060767.jpg"
				}
			},
			"name": "Canada Goose Langford Slim Fit Down Parka with Genuine Coyote Fur Trim",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,050.00",
					"maxItemPrice": "1,050.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-langford-slim-fit-down-parka-with-genuine-coyote-fur-trim/3218760",
			"reviewCount": 48,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"3269115": {
			"id": 3269115,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "529107",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_101537242",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"2_101537242",
						"16_101470696",
						"12_101537572"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "2_101537242"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_101537572": {
					"id": "12_101537572",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_101537572.jpg"
				},
				"16_101470696": {
					"id": "16_101470696",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_101470696.jpg"
				},
				"2_101537242": {
					"id": "2_101537242",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101537242.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Regular Fit 4-Pack Supima® Cotton T-Shirts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-regular-fit-4-pack-supima-cotton-t-shirts/3269115",
			"reviewCount": 249,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"3269117": {
			"id": 3269117,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "529124",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_7076529",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"9_7076529",
						"10_105978130",
						"11_9090811"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "9_7076529"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_105978130": {
					"id": "10_105978130",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_105978130.jpg"
				},
				"11_9090811": {
					"id": "11_9090811",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_9090811.jpg"
				},
				"9_7076529": {
					"id": "9_7076529",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_7076529.jpg"
				}
			},
			"name": "Nordstrom Men's Shop 4-Pack Supima® Cotton Athletic Tanks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.50",
					"maxItemPrice": "34.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-4-pack-supima-cotton-athletic-tanks/3269117",
			"reviewCount": 96,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"3269152": {
			"id": 3269152,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "529136",
			"colorCount": 3,
			"colorDefaultId": "navy/ charcoal/ blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_101057050-14_7084674-11_105571531",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_7084674",
						"1_12385221",
						"12_12385192"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_7084674"
				},
				"navy/ charcoal/ blue": {
					"id": "navy/ charcoal/ blue",
					"label": "NAVY/ CHARCOAL/ BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"10_101057050",
						"3_101057043",
						"3_101069583"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_101057050"
				},
				"navy/ charcoal/ blue stripe": {
					"id": "navy/ charcoal/ blue stripe",
					"label": "NAVY/ CHARCOAL/ BLUE STRIPE",
					"spriteIndex": 2,
					"mediaIds": [
						"11_105571531",
						"17_105571537",
						"12_105616092"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_105571531"
				}
			},
			"colorIds": [
				"navy/ charcoal/ blue",
				"black",
				"navy/ charcoal/ blue stripe"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_101057050": {
					"id": "10_101057050",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_101057050.jpg"
				},
				"11_105571531": {
					"id": "11_105571531",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105571531.jpg"
				},
				"12_105616092": {
					"id": "12_105616092",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105616092.jpg"
				},
				"12_12385192": {
					"id": "12_12385192",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_12385192.jpg"
				},
				"14_7084674": {
					"id": "14_7084674",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_7084674.jpg"
				},
				"17_105571537": {
					"id": "17_105571537",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105571537.jpg"
				},
				"1_12385221": {
					"id": "1_12385221",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_12385221.jpg"
				},
				"3_101057043": {
					"id": "3_101057043",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101057043.jpg"
				},
				"3_101069583": {
					"id": "3_101069583",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101069583.jpg"
				}
			},
			"name": "Nordstrom Men's Shop 3-Pack Supima® Cotton Boxer Briefs",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.50",
					"maxItemPrice": "34.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-3-pack-supima-cotton-boxer-briefs/3269152",
			"reviewCount": 165,
			"reviewStarRating": 4.2,
			"storeAvailability": null
		},
		"3269153": {
			"id": 3269153,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "529142",
			"colorCount": 2,
			"colorDefaultId": "navy/ charcoal/ blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_101055785-14_7084694",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_7084694",
						"2_105580582",
						"2_105611462"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_7084694"
				},
				"navy/ charcoal/ blue": {
					"id": "navy/ charcoal/ blue",
					"label": "NAVY/ CHARCOAL/ BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"5_101055785",
						"18_101055778",
						"9_101069549"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_101055785"
				}
			},
			"colorIds": [
				"navy/ charcoal/ blue",
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_7084694": {
					"id": "14_7084694",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_7084694.jpg"
				},
				"18_101055778": {
					"id": "18_101055778",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_101055778.jpg"
				},
				"2_105580582": {
					"id": "2_105580582",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105580582.jpg"
				},
				"2_105611462": {
					"id": "2_105611462",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105611462.jpg"
				},
				"5_101055785": {
					"id": "5_101055785",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_101055785.jpg"
				},
				"9_101069549": {
					"id": "9_101069549",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101069549.jpg"
				}
			},
			"name": "Nordstrom Men's Shop 3-Pack Supima® Cotton Boxers",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.50",
					"maxItemPrice": "34.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-3-pack-supima-cotton-boxers/3269153",
			"reviewCount": 131,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"3311139": {
			"id": 3311139,
			"brandId": 6832,
			"brandName": "TOMMY JOHN",
			"styleNumber": "560092",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_102492013",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_102492013",
						"12_102492012",
						"1_102491681"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "13_102492013"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_102492012": {
					"id": "12_102492012",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_102492012.jpg"
				},
				"13_102492013": {
					"id": "13_102492013",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_102492013.jpg"
				},
				"1_102491681": {
					"id": "1_102491681",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_102491681.jpg"
				}
			},
			"name": "Tommy John Cool Cotton High V-Neck Undershirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "40.00",
					"maxItemPrice": "40.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/tommy-john-cool-cotton-high-v-neck-undershirt/3311139",
			"reviewCount": 16,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"3341452": {
			"id": 3341452,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "581016",
			"colorCount": 5,
			"colorDefaultId": "blue dazzle solid- plaid pack",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_103053109-15_104870435-4_105828404-19_106720039-18_105837738",
			"colorsById": {
				"black- white plaid pack": {
					"id": "black- white plaid pack",
					"label": "BLACK- WHITE PLAID PACK",
					"spriteIndex": 1,
					"mediaIds": [
						"15_104870435",
						"13_104870393",
						"19_104910219"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "15_104870435"
				},
				"blue dazzle solid- plaid pack": {
					"id": "blue dazzle solid- plaid pack",
					"label": "BLUE DAZZLE SOLID- PLAID PACK",
					"spriteIndex": 0,
					"mediaIds": [
						"9_103053109",
						"13_103053113",
						"3_103096403"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_103053109"
				},
				"blue eoe/ white": {
					"id": "blue eoe/ white",
					"label": "BLUE EOE/ WHITE",
					"spriteIndex": 2,
					"mediaIds": [
						"4_105828404",
						"5_105828385",
						"4_9278344"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_105828404"
				},
				"navy peacoat stripe plaid pack": {
					"id": "navy peacoat stripe plaid pack",
					"label": "NAVY PEACOAT STRIPE PLAID PACK",
					"spriteIndex": 3,
					"mediaIds": [
						"19_106720039",
						"4_106720044",
						"3_103096403"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_106720039"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 4,
					"mediaIds": [
						"18_105837738",
						"6_105825986",
						"11_105837731"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "18_105837738"
				}
			},
			"colorIds": [
				"blue dazzle solid- plaid pack",
				"black- white plaid pack",
				"blue eoe/ white",
				"navy peacoat stripe plaid pack",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_105837731": {
					"id": "11_105837731",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105837731.jpg"
				},
				"13_103053113": {
					"id": "13_103053113",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_103053113.jpg"
				},
				"13_104870393": {
					"id": "13_104870393",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104870393.jpg"
				},
				"15_104870435": {
					"id": "15_104870435",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104870435.jpg"
				},
				"18_105837738": {
					"id": "18_105837738",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105837738.jpg"
				},
				"19_104910219": {
					"id": "19_104910219",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104910219.jpg"
				},
				"19_106720039": {
					"id": "19_106720039",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106720039.jpg"
				},
				"3_103096403": {
					"id": "3_103096403",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_103096403.jpg"
				},
				"4_105828404": {
					"id": "4_105828404",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105828404.jpg"
				},
				"4_106720044": {
					"id": "4_106720044",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106720044.jpg"
				},
				"4_9278344": {
					"id": "4_9278344",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_9278344.jpg"
				},
				"5_105828385": {
					"id": "5_105828385",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105828385.jpg"
				},
				"6_105825986": {
					"id": "6_105825986",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105825986.jpg"
				},
				"9_103053109": {
					"id": "9_103053109",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_103053109.jpg"
				}
			},
			"name": "Nordstrom Men's Shop 3-Pack Classic Fit Boxers",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-3-pack-classic-fit-boxers/3341452",
			"reviewCount": 172,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"3509958": {
			"id": 3509958,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "901676",
			"colorCount": 4,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107048276-2_104133582-8_101797648-4_107048304",
			"colorsById": {
				"black / red": {
					"id": "black / red",
					"label": "BLACK / RED",
					"spriteIndex": 1,
					"mediaIds": [
						"2_104133582",
						"0_104133540",
						"14_104134334"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "2_104133582"
				},
				"black/graphite": {
					"id": "black/graphite",
					"label": "BLACK/GRAPHITE",
					"spriteIndex": 2,
					"mediaIds": [
						"8_101797648",
						"2_101797762",
						"3_101797763"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_101797648"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107048276",
						"18_107048338",
						"15_107048335"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_107048276"
				},
				"red": {
					"id": "red",
					"label": "RED",
					"spriteIndex": 3,
					"mediaIds": [
						"4_107048304",
						"7_107048347",
						"6_107048346"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "4_107048304"
				}
			},
			"colorIds": [
				"navy",
				"black / red",
				"black/graphite",
				"red"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_104133540": {
					"id": "0_104133540",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_104133540.jpg"
				},
				"14_104134334": {
					"id": "14_104134334",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104134334.jpg"
				},
				"15_107048335": {
					"id": "15_107048335",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107048335.jpg"
				},
				"16_107048276": {
					"id": "16_107048276",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107048276.jpg"
				},
				"18_107048338": {
					"id": "18_107048338",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107048338.jpg"
				},
				"2_101797762": {
					"id": "2_101797762",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101797762.jpg"
				},
				"2_104133582": {
					"id": "2_104133582",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_104133582.jpg"
				},
				"3_101797763": {
					"id": "3_101797763",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101797763.jpg"
				},
				"4_107048304": {
					"id": "4_107048304",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107048304.jpg"
				},
				"6_107048346": {
					"id": "6_107048346",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107048346.jpg"
				},
				"7_107048347": {
					"id": "7_107048347",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107048347.jpg"
				},
				"8_101797648": {
					"id": "8_101797648",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_101797648.jpg"
				}
			},
			"name": "Canada Goose 'Hybridge™ Lite Hoody' Slim Fit Packable Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "595.00",
					"maxItemPrice": "595.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-hybridge-lite-hoody-slim-fit-packable-jacket/3509958",
			"reviewCount": 16,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"3524814": {
			"id": 3524814,
			"brandId": 6832,
			"brandName": "TOMMY JOHN",
			"styleNumber": "912992",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_12165631",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"11_12165631",
						"6_12165626",
						"16_12165596"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "11_12165631"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_12165631": {
					"id": "11_12165631",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_12165631.jpg"
				},
				"16_12165596": {
					"id": "16_12165596",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_12165596.jpg"
				},
				"6_12165626": {
					"id": "6_12165626",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_12165626.jpg"
				}
			},
			"name": "Tommy John Second Skin High V-Neck Undershirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "43.00",
					"maxItemPrice": "43.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/tommy-john-second-skin-high-v-neck-undershirt/3524814",
			"reviewCount": 12,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"3542353": {
			"id": 3542353,
			"brandId": 7450,
			"brandName": "NAKED AND FAMOUS",
			"styleNumber": "924571",
			"colorCount": 1,
			"colorDefaultId": "stretch selvedge",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_104592493",
			"colorsById": {
				"stretch selvedge": {
					"id": "stretch selvedge",
					"label": "STRETCH SELVEDGE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_104592493",
						"6_104615526",
						"4_8326204"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_104592493"
				}
			},
			"colorIds": [
				"stretch selvedge"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_104592493": {
					"id": "13_104592493",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104592493.jpg"
				},
				"4_8326204": {
					"id": "4_8326204",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_8326204.jpg"
				},
				"6_104615526": {
					"id": "6_104615526",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_104615526.jpg"
				}
			},
			"name": "Naked & Famous Denim Weird Guy Slim Fit Raw Jeans (Stretch Selvedge)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "158.00",
					"maxItemPrice": "158.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "79.00",
					"maxItemPrice": "79.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/naked-famous-denim-weird-guy-slim-fit-raw-jeans-stretch-selvedge/3542353",
			"reviewCount": 7,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"3609490": {
			"id": 3609490,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "973902",
			"colorCount": 1,
			"colorDefaultId": "navy/ white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_107214964",
			"colorsById": {
				"navy/ white": {
					"id": "navy/ white",
					"label": "NAVY/ WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"4_107214964",
						"13_8774993",
						"11_8774891"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_107214964"
				}
			},
			"colorIds": [
				"navy/ white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_8774891": {
					"id": "11_8774891",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_8774891.jpg"
				},
				"13_8774993": {
					"id": "13_8774993",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_8774993.jpg"
				},
				"4_107214964": {
					"id": "4_107214964",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107214964.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Slim Fit Stripe T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "156.00",
					"maxItemPrice": "156.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-slim-fit-stripe-t-shirt/3609490",
			"reviewCount": 8,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"3609688": {
			"id": 3609688,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "974044",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_8774580",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"0_8774580",
						"17_102485417",
						"11_102485551"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_8774580"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_8774580": {
					"id": "0_8774580",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_8774580.jpg"
				},
				"11_102485551": {
					"id": "11_102485551",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_102485551.jpg"
				},
				"17_102485417": {
					"id": "17_102485417",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_102485417.jpg"
				}
			},
			"name": "Comme des Garçons PLAY X-Ray Heart Logo Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "125.00",
					"maxItemPrice": "125.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-x-ray-heart-logo-graphic-tee/3609688",
			"reviewCount": 28,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"3609773": {
			"id": 3609773,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "974100",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_8776215",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"15_8776215",
						"6_13159806",
						"11_13159771"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "15_8776215"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_13159771": {
					"id": "11_13159771",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_13159771.jpg"
				},
				"15_8776215": {
					"id": "15_8776215",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_8776215.jpg"
				},
				"6_13159806": {
					"id": "6_13159806",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_13159806.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Zip-Up Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "314.00",
					"maxItemPrice": "314.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-zip-up-hoodie/3609773",
			"reviewCount": 14,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"3678537": {
			"id": 3678537,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "519066",
			"colorCount": 3,
			"colorDefaultId": "mid grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_107741555-7_103017127-5_106736405",
			"colorsById": {
				"light grey": {
					"id": "light grey",
					"label": "LIGHT GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"7_103017127",
						"10_103017130",
						"9_103017069"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "7_103017127"
				},
				"mid grey": {
					"id": "mid grey",
					"label": "MID GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"15_107741555",
						"4_107741904",
						"5_107741545"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "15_107741555"
				},
				"taupe": {
					"id": "taupe",
					"label": "TAUPE",
					"spriteIndex": 2,
					"mediaIds": [
						"5_106736405",
						"10_107734350",
						"11_107734351"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_106736405"
				}
			},
			"colorIds": [
				"mid grey",
				"light grey",
				"taupe"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_103017130": {
					"id": "10_103017130",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_103017130.jpg"
				},
				"10_107734350": {
					"id": "10_107734350",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107734350.jpg"
				},
				"11_107734351": {
					"id": "11_107734351",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107734351.jpg"
				},
				"15_107741555": {
					"id": "15_107741555",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107741555.jpg"
				},
				"4_107741904": {
					"id": "4_107741904",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107741904.jpg"
				},
				"5_106736405": {
					"id": "5_106736405",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106736405.jpg"
				},
				"5_107741545": {
					"id": "5_107741545",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107741545.jpg"
				},
				"7_103017127": {
					"id": "7_103017127",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103017127.jpg"
				},
				"9_103017069": {
					"id": "9_103017069",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_103017069.jpg"
				}
			},
			"name": "Ted Baker London Jefferson Flat Front Wool Dress Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "198.00",
					"maxItemPrice": "198.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-jefferson-flat-front-wool-dress-pants/3678537",
			"reviewCount": 73,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"3704584": {
			"id": 3704584,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "497828",
			"colorCount": 5,
			"colorDefaultId": "tan",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_105678854-17_101820237-13_106739173-12_101972092-8_101277928",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"17_101820237",
						"4_101820244",
						"2_101820182"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "17_101820237"
				},
				"grey tornado": {
					"id": "grey tornado",
					"label": "GREY TORNADO",
					"spriteIndex": 2,
					"mediaIds": [
						"13_106739173",
						"13_13428073",
						"6_101983026"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "13_106739173"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"12_101972092",
						"8_103630748",
						"12_9145692"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_101972092"
				},
				"tan": {
					"id": "tan",
					"label": "TAN",
					"spriteIndex": 0,
					"mediaIds": [
						"14_105678854",
						"2_105678822",
						"19_105678779"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "14_105678854"
				},
				"taupe": {
					"id": "taupe",
					"label": "TAUPE",
					"spriteIndex": 4,
					"mediaIds": [
						"8_101277928",
						"18_100034578",
						"3_101277903"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "8_101277928"
				}
			},
			"colorIds": [
				"tan",
				"black",
				"grey tornado",
				"navy",
				"taupe"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_101972092": {
					"id": "12_101972092",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_101972092.jpg"
				},
				"12_9145692": {
					"id": "12_9145692",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_9145692.jpg"
				},
				"13_106739173": {
					"id": "13_106739173",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106739173.jpg"
				},
				"13_13428073": {
					"id": "13_13428073",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_13428073.jpg"
				},
				"14_105678854": {
					"id": "14_105678854",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105678854.jpg"
				},
				"17_101820237": {
					"id": "17_101820237",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_101820237.jpg"
				},
				"18_100034578": {
					"id": "18_100034578",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_100034578.jpg"
				},
				"19_105678779": {
					"id": "19_105678779",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105678779.jpg"
				},
				"2_101820182": {
					"id": "2_101820182",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101820182.jpg"
				},
				"2_105678822": {
					"id": "2_105678822",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105678822.jpg"
				},
				"3_101277903": {
					"id": "3_101277903",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101277903.jpg"
				},
				"4_101820244": {
					"id": "4_101820244",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101820244.jpg"
				},
				"6_101983026": {
					"id": "6_101983026",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_101983026.jpg"
				},
				"8_101277928": {
					"id": "8_101277928",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_101277928.jpg"
				},
				"8_103630748": {
					"id": "8_103630748",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_103630748.jpg"
				}
			},
			"name": "Nordstrom Men's Shop 'Classic' Smartcare™ Relaxed Fit Double Pleated Cotton Pants (Online Only)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-classic-smartcare-relaxed-fit-double-pleated-cotton-pants-online-only/3704584",
			"reviewCount": 217,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"3704600": {
			"id": 3704600,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "499261",
			"colorCount": 5,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_9146173-14_101975014-5_100206825-12_9146332-2_9146262",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_101975014",
						"11_9146031",
						"6_9146006"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_101975014"
				},
				"grey tornado": {
					"id": "grey tornado",
					"label": "GREY TORNADO",
					"spriteIndex": 2,
					"mediaIds": [
						"5_100206825",
						"8_100207108",
						"2_100205882"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_100206825"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"13_9146173",
						"2_9146162",
						"4_101461724"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_9146173"
				},
				"tan": {
					"id": "tan",
					"label": "TAN",
					"spriteIndex": 3,
					"mediaIds": [
						"12_9146332",
						"1_9327061",
						"7_9327067"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "12_9146332"
				},
				"taupe": {
					"id": "taupe",
					"label": "TAUPE",
					"spriteIndex": 4,
					"mediaIds": [
						"2_9146262",
						"6_13063046",
						"11_101461611"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "2_9146262"
				}
			},
			"colorIds": [
				"navy",
				"black",
				"grey tornado",
				"tan",
				"taupe"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_101461611": {
					"id": "11_101461611",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_101461611.jpg"
				},
				"11_9146031": {
					"id": "11_9146031",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_9146031.jpg"
				},
				"12_9146332": {
					"id": "12_9146332",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_9146332.jpg"
				},
				"13_9146173": {
					"id": "13_9146173",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_9146173.jpg"
				},
				"14_101975014": {
					"id": "14_101975014",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_101975014.jpg"
				},
				"1_9327061": {
					"id": "1_9327061",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_9327061.jpg"
				},
				"2_100205882": {
					"id": "2_100205882",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_100205882.jpg"
				},
				"2_9146162": {
					"id": "2_9146162",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_9146162.jpg"
				},
				"2_9146262": {
					"id": "2_9146262",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_9146262.jpg"
				},
				"4_101461724": {
					"id": "4_101461724",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101461724.jpg"
				},
				"5_100206825": {
					"id": "5_100206825",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_100206825.jpg"
				},
				"6_13063046": {
					"id": "6_13063046",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_13063046.jpg"
				},
				"6_9146006": {
					"id": "6_9146006",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_9146006.jpg"
				},
				"7_9327067": {
					"id": "7_9327067",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_9327067.jpg"
				},
				"8_100207108": {
					"id": "8_100207108",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_100207108.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Classic Smartcare™ Relaxed Fit Flat Front Cotton Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-classic-smartcare-relaxed-fit-flat-front-cotton-pants/3704600",
			"reviewCount": 181,
			"reviewStarRating": 3.8,
			"storeAvailability": null
		},
		"3721841": {
			"id": 3721841,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "437395",
			"colorCount": 3,
			"colorDefaultId": "grey shade marl",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_105790818-17_105703297-16_105705856",
			"colorsById": {
				"black caviar": {
					"id": "black caviar",
					"label": "BLACK CAVIAR",
					"spriteIndex": 1,
					"mediaIds": [
						"17_105703297",
						"3_12792483",
						"19_12792499"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "17_105703297"
				},
				"grey shade marl": {
					"id": "grey shade marl",
					"label": "GREY SHADE MARL",
					"spriteIndex": 0,
					"mediaIds": [
						"18_105790818",
						"7_105790887",
						"4_101209124"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_105790818"
				},
				"navy iris": {
					"id": "navy iris",
					"label": "NAVY IRIS",
					"spriteIndex": 2,
					"mediaIds": [
						"16_105705856",
						"2_105706102",
						"18_105705858"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_105705856"
				}
			},
			"colorIds": [
				"grey shade marl",
				"black caviar",
				"navy iris"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_105705856": {
					"id": "16_105705856",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105705856.jpg"
				},
				"17_105703297": {
					"id": "17_105703297",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105703297.jpg"
				},
				"18_105705858": {
					"id": "18_105705858",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105705858.jpg"
				},
				"18_105790818": {
					"id": "18_105790818",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105790818.jpg"
				},
				"19_12792499": {
					"id": "19_12792499",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_12792499.jpg"
				},
				"2_105706102": {
					"id": "2_105706102",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105706102.jpg"
				},
				"3_12792483": {
					"id": "3_12792483",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_12792483.jpg"
				},
				"4_101209124": {
					"id": "4_101209124",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101209124.jpg"
				},
				"7_105790887": {
					"id": "7_105790887",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105790887.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Cotton & Cashmere V-Neck Sweater",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "49.50",
					"maxItemPrice": "49.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-cotton-cashmere-v-neck-sweater/3721841",
			"reviewCount": 218,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"3736650": {
			"id": 3736650,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "411848",
			"colorCount": 2,
			"colorDefaultId": "navy iris",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_105828372-0_105703680",
			"colorsById": {
				"black caviar": {
					"id": "black caviar",
					"label": "BLACK CAVIAR",
					"spriteIndex": 1,
					"mediaIds": [
						"0_105703680",
						"2_101181502",
						"18_101181418"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_105703680"
				},
				"navy iris": {
					"id": "navy iris",
					"label": "NAVY IRIS",
					"spriteIndex": 0,
					"mediaIds": [
						"12_105828372",
						"16_105828536",
						"10_103547390"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_105828372"
				}
			},
			"colorIds": [
				"navy iris",
				"black caviar"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_105703680": {
					"id": "0_105703680",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105703680.jpg"
				},
				"10_103547390": {
					"id": "10_103547390",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_103547390.jpg"
				},
				"12_105828372": {
					"id": "12_105828372",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105828372.jpg"
				},
				"16_105828536": {
					"id": "16_105828536",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105828536.jpg"
				},
				"18_101181418": {
					"id": "18_101181418",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_101181418.jpg"
				},
				"2_101181502": {
					"id": "2_101181502",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101181502.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Half Zip Cotton & Cashmere Pullover (Regular & Tall)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-half-zip-cotton-cashmere-pullover-regular-tall/3736650",
			"reviewCount": 139,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"3752827": {
			"id": 3752827,
			"brandId": 168,
			"brandName": "Cutter & Buck",
			"styleNumber": "475824",
			"colorCount": 4,
			"colorDefaultId": "seaport blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_9167321-12_9166452-19_9167299-19_9371219",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"12_9166452",
						"5_9430145",
						"15_9430175"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_9166452"
				},
				"sea blue": {
					"id": "sea blue",
					"label": "SEA BLUE",
					"spriteIndex": 2,
					"mediaIds": [
						"19_9167299",
						"17_12724237",
						"18_12724118"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_9167299"
				},
				"seaport blue": {
					"id": "seaport blue",
					"label": "SEAPORT BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"1_9167321",
						"12_12723872",
						"1_12723801"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "1_9167321"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 3,
					"mediaIds": [
						"19_9371219",
						"19_9379259",
						"12_9379112"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "19_9371219"
				}
			},
			"colorIds": [
				"seaport blue",
				"black",
				"sea blue",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_12723872": {
					"id": "12_12723872",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_12723872.jpg"
				},
				"12_9166452": {
					"id": "12_9166452",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_9166452.jpg"
				},
				"12_9379112": {
					"id": "12_9379112",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_9379112.jpg"
				},
				"15_9430175": {
					"id": "15_9430175",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_9430175.jpg"
				},
				"17_12724237": {
					"id": "17_12724237",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_12724237.jpg"
				},
				"18_12724118": {
					"id": "18_12724118",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_12724118.jpg"
				},
				"19_9167299": {
					"id": "19_9167299",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_9167299.jpg"
				},
				"19_9371219": {
					"id": "19_9371219",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_9371219.jpg"
				},
				"19_9379259": {
					"id": "19_9379259",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_9379259.jpg"
				},
				"1_12723801": {
					"id": "1_12723801",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_12723801.jpg"
				},
				"1_9167321": {
					"id": "1_9167321",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_9167321.jpg"
				},
				"5_9430145": {
					"id": "5_9430145",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_9430145.jpg"
				}
			},
			"name": "Cutter & Buck Genre DryTec Moisture Wicking Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "60.00",
					"maxItemPrice": "60.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "60.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cutter-buck-genre-drytec-moisture-wicking-polo/3752827",
			"reviewCount": 49,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"3943102": {
			"id": 3943102,
			"brandId": 9074,
			"brandName": "FRAME",
			"styleNumber": "1036923",
			"colorCount": 1,
			"colorDefaultId": "burrard",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107601218",
			"colorsById": {
				"burrard": {
					"id": "burrard",
					"label": "BURRARD",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107601218",
						"2_107627442",
						"1_107627441"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_107601218"
				}
			},
			"colorIds": [
				"burrard"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"18_107601218": {
					"id": "18_107601218",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107601218.jpg"
				},
				"1_107627441": {
					"id": "1_107627441",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107627441.jpg"
				},
				"2_107627442": {
					"id": "2_107627442",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107627442.jpg"
				}
			},
			"name": "FRAME L'Homme Slim Fit Jeans (Burrard)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "205.00",
					"maxItemPrice": "205.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/frame-lhomme-slim-fit-jeans-burrard/3943102",
			"reviewCount": 2,
			"reviewStarRating": 3.5,
			"storeAvailability": null
		},
		"3986505": {
			"id": 3986505,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "1070334",
			"colorCount": 4,
			"colorDefaultId": "graphite",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_103854791-1_103843981-14_103854694-15_103854655",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"1_103843981",
						"8_103843928",
						"12_11758432"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "1_103843981"
				},
				"graphite": {
					"id": "graphite",
					"label": "GRAPHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"11_103854791",
						"3_103854803",
						"14_103854754"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "11_103854791"
				},
				"military green": {
					"id": "military green",
					"label": "MILITARY GREEN",
					"spriteIndex": 2,
					"mediaIds": [
						"14_103854694",
						"16_103854676",
						"10_103854750"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "14_103854694"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"15_103854655",
						"16_103854656",
						"18_103854698"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_103854655"
				}
			},
			"colorIds": [
				"graphite",
				"black",
				"military green",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_103854750": {
					"id": "10_103854750",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_103854750.jpg"
				},
				"11_103854791": {
					"id": "11_103854791",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_103854791.jpg"
				},
				"12_11758432": {
					"id": "12_11758432",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_11758432.jpg"
				},
				"14_103854694": {
					"id": "14_103854694",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103854694.jpg"
				},
				"14_103854754": {
					"id": "14_103854754",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103854754.jpg"
				},
				"15_103854655": {
					"id": "15_103854655",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_103854655.jpg"
				},
				"16_103854656": {
					"id": "16_103854656",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103854656.jpg"
				},
				"16_103854676": {
					"id": "16_103854676",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103854676.jpg"
				},
				"18_103854698": {
					"id": "18_103854698",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103854698.jpg"
				},
				"1_103843981": {
					"id": "1_103843981",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103843981.jpg"
				},
				"3_103854803": {
					"id": "3_103854803",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_103854803.jpg"
				},
				"8_103843928": {
					"id": "8_103843928",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_103843928.jpg"
				}
			},
			"name": "Canada Goose 'Carson' Slim Fit Hooded Parka with Genuine Coyote Fur Trim",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,095.00",
					"maxItemPrice": "1,095.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-carson-slim-fit-hooded-parka-with-genuine-coyote-fur-trim/3986505",
			"reviewCount": 29,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"3997606": {
			"id": 3997606,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "1034203",
			"colorCount": 1,
			"colorDefaultId": "top dyed gray",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_101891521",
			"colorsById": {
				"top dyed gray": {
					"id": "top dyed gray",
					"label": "TOP DYED GRAY",
					"spriteIndex": 0,
					"mediaIds": [
						"1_101891521",
						"14_101891514",
						"6_101891626"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "1_101891521"
				}
			},
			"colorIds": [
				"top dyed gray"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_101891514": {
					"id": "14_101891514",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_101891514.jpg"
				},
				"1_101891521": {
					"id": "1_101891521",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_101891521.jpg"
				},
				"6_101891626": {
					"id": "6_101891626",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_101891626.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Logo Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "130.00",
					"maxItemPrice": "130.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-logo-graphic-tee/3997606",
			"reviewCount": 6,
			"reviewStarRating": 3.7,
			"storeAvailability": null
		},
		"4002995": {
			"id": 4002995,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "1083758",
			"colorCount": 9,
			"colorDefaultId": "white brilliant",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_106003997-4_105364664-3_105874563-8_106003848-9_105372029-17_105358017-16_105371996-19_105869959-2_106997362",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"4_105364664",
						"8_105364648",
						"11_105363531"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "4_105364664"
				},
				"blue azurite": {
					"id": "blue azurite",
					"label": "BLUE AZURITE",
					"spriteIndex": 2,
					"mediaIds": [
						"3_105874563",
						"5_105874265",
						"6_106003946"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "3_105874563"
				},
				"blue surf": {
					"id": "blue surf",
					"label": "BLUE SURF",
					"spriteIndex": 3,
					"mediaIds": [
						"8_106003848",
						"12_106003852",
						"6_106003946"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_106003848"
				},
				"grey castlerock": {
					"id": "grey castlerock",
					"label": "GREY CASTLEROCK",
					"spriteIndex": 4,
					"mediaIds": [
						"9_105372029",
						"7_105371967",
						"19_105372319"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_105372029"
				},
				"navy medieval": {
					"id": "navy medieval",
					"label": "NAVY MEDIEVAL",
					"spriteIndex": 5,
					"mediaIds": [
						"17_105358017",
						"0_105358040",
						"12_105358092"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "17_105358017"
				},
				"pink breath": {
					"id": "pink breath",
					"label": "PINK BREATH",
					"spriteIndex": 6,
					"mediaIds": [
						"16_105371996",
						"18_105371938",
						"1_105357961"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "16_105371996"
				},
				"purple regal": {
					"id": "purple regal",
					"label": "PURPLE REGAL",
					"spriteIndex": 7,
					"mediaIds": [
						"19_105869959",
						"2_105869962",
						"6_106003946"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "19_105869959"
				},
				"red ruby": {
					"id": "red ruby",
					"label": "RED RUBY",
					"spriteIndex": 8,
					"mediaIds": [
						"2_106997362",
						"5_107000145",
						"6_106003946"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "2_106997362"
				},
				"white brilliant": {
					"id": "white brilliant",
					"label": "WHITE BRILLIANT",
					"spriteIndex": 0,
					"mediaIds": [
						"17_106003997",
						"19_106003999",
						"6_106003946"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "17_106003997"
				}
			},
			"colorIds": [
				"white brilliant",
				"black",
				"blue azurite",
				"blue surf",
				"grey castlerock",
				"navy medieval",
				"pink breath",
				"purple regal",
				"red ruby"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_105358040": {
					"id": "0_105358040",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105358040.jpg"
				},
				"11_105363531": {
					"id": "11_105363531",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105363531.jpg"
				},
				"12_105358092": {
					"id": "12_105358092",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105358092.jpg"
				},
				"12_106003852": {
					"id": "12_106003852",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106003852.jpg"
				},
				"16_105371996": {
					"id": "16_105371996",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105371996.jpg"
				},
				"17_105358017": {
					"id": "17_105358017",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105358017.jpg"
				},
				"17_106003997": {
					"id": "17_106003997",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106003997.jpg"
				},
				"18_105371938": {
					"id": "18_105371938",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105371938.jpg"
				},
				"19_105372319": {
					"id": "19_105372319",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105372319.jpg"
				},
				"19_105869959": {
					"id": "19_105869959",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105869959.jpg"
				},
				"19_106003999": {
					"id": "19_106003999",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106003999.jpg"
				},
				"1_105357961": {
					"id": "1_105357961",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105357961.jpg"
				},
				"2_105869962": {
					"id": "2_105869962",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105869962.jpg"
				},
				"2_106997362": {
					"id": "2_106997362",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106997362.jpg"
				},
				"3_105874563": {
					"id": "3_105874563",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105874563.jpg"
				},
				"4_105364664": {
					"id": "4_105364664",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105364664.jpg"
				},
				"5_105874265": {
					"id": "5_105874265",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105874265.jpg"
				},
				"5_107000145": {
					"id": "5_107000145",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107000145.jpg"
				},
				"6_106003946": {
					"id": "6_106003946",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106003946.jpg"
				},
				"7_105371967": {
					"id": "7_105371967",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105371967.jpg"
				},
				"8_105364648": {
					"id": "8_105364648",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105364648.jpg"
				},
				"8_106003848": {
					"id": "8_106003848",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106003848.jpg"
				},
				"9_105372029": {
					"id": "9_105372029",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_105372029.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Trim Fit Non-Iron Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-trim-fit-non-iron-dress-shirt/4002995",
			"reviewCount": 235,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4020089": {
			"id": 4020089,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "1099232",
			"colorCount": 6,
			"colorDefaultId": "white brilliant",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_105870068-18_105372498-11_105863531-4_105570364-9_105352229-13_105358333",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"18_105372498",
						"5_105372445",
						"4_105358084"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_105372498"
				},
				"blue azurite": {
					"id": "blue azurite",
					"label": "BLUE AZURITE",
					"spriteIndex": 2,
					"mediaIds": [
						"11_105863531",
						"15_105863535",
						"8_105863508"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_105863531"
				},
				"blue surf": {
					"id": "blue surf",
					"label": "BLUE SURF",
					"spriteIndex": 3,
					"mediaIds": [
						"4_105570364",
						"3_105570363",
						"2_105570362"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_105570364"
				},
				"grey castlerock": {
					"id": "grey castlerock",
					"label": "GREY CASTLEROCK",
					"spriteIndex": 4,
					"mediaIds": [
						"9_105352229",
						"11_105352191",
						"19_105351559"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_105352229"
				},
				"navy medieval": {
					"id": "navy medieval",
					"label": "NAVY MEDIEVAL",
					"spriteIndex": 5,
					"mediaIds": [
						"13_105358333",
						"1_105358321",
						"0_105351900"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_105358333"
				},
				"white brilliant": {
					"id": "white brilliant",
					"label": "WHITE BRILLIANT",
					"spriteIndex": 0,
					"mediaIds": [
						"8_105870068",
						"1_105870021",
						"14_105870054"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "8_105870068"
				}
			},
			"colorIds": [
				"white brilliant",
				"black",
				"blue azurite",
				"blue surf",
				"grey castlerock",
				"navy medieval"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_105351900": {
					"id": "0_105351900",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105351900.jpg"
				},
				"11_105352191": {
					"id": "11_105352191",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105352191.jpg"
				},
				"11_105863531": {
					"id": "11_105863531",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105863531.jpg"
				},
				"13_105358333": {
					"id": "13_105358333",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_105358333.jpg"
				},
				"14_105870054": {
					"id": "14_105870054",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105870054.jpg"
				},
				"15_105863535": {
					"id": "15_105863535",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105863535.jpg"
				},
				"18_105372498": {
					"id": "18_105372498",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105372498.jpg"
				},
				"19_105351559": {
					"id": "19_105351559",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105351559.jpg"
				},
				"1_105358321": {
					"id": "1_105358321",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105358321.jpg"
				},
				"1_105870021": {
					"id": "1_105870021",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105870021.jpg"
				},
				"2_105570362": {
					"id": "2_105570362",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105570362.jpg"
				},
				"3_105570363": {
					"id": "3_105570363",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105570363.jpg"
				},
				"4_105358084": {
					"id": "4_105358084",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105358084.jpg"
				},
				"4_105570364": {
					"id": "4_105570364",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105570364.jpg"
				},
				"5_105372445": {
					"id": "5_105372445",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105372445.jpg"
				},
				"8_105863508": {
					"id": "8_105863508",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105863508.jpg"
				},
				"8_105870068": {
					"id": "8_105870068",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105870068.jpg"
				},
				"9_105352229": {
					"id": "9_105352229",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_105352229.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Classic Fit Non-Iron Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-classic-fit-non-iron-dress-shirt/4020089",
			"reviewCount": 102,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"4024667": {
			"id": 4024667,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "1103561",
			"colorCount": 6,
			"colorDefaultId": "northern night",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_106484507-0_101974280-3_101333583-15_13446875-16_13447436-18_13447318",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"0_101974280",
						"5_11519585",
						"2_11519582"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_101974280"
				},
				"graphite": {
					"id": "graphite",
					"label": "GRAPHITE",
					"spriteIndex": 2,
					"mediaIds": [
						"3_101333583",
						"14_13167654",
						"10_13167730"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_101333583"
				},
				"military green": {
					"id": "military green",
					"label": "MILITARY GREEN",
					"spriteIndex": 3,
					"mediaIds": [
						"15_13446875",
						"9_13446869",
						"11_13446851"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "15_13446875"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 4,
					"mediaIds": [
						"16_13447436",
						"15_13447435",
						"3_13447483"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_13447436"
				},
				"northern night": {
					"id": "northern night",
					"label": "NORTHERN NIGHT",
					"spriteIndex": 0,
					"mediaIds": [
						"7_106484507",
						"11_106484571",
						"7_106484567"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_106484507"
				},
				"red": {
					"id": "red",
					"label": "RED",
					"spriteIndex": 5,
					"mediaIds": [
						"18_13447318",
						"17_13447317",
						"17_13447297"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "18_13447318"
				}
			},
			"colorIds": [
				"northern night",
				"black",
				"graphite",
				"military green",
				"navy",
				"red"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_101974280": {
					"id": "0_101974280",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_101974280.jpg"
				},
				"10_13167730": {
					"id": "10_13167730",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_13167730.jpg"
				},
				"11_106484571": {
					"id": "11_106484571",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106484571.jpg"
				},
				"11_13446851": {
					"id": "11_13446851",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_13446851.jpg"
				},
				"14_13167654": {
					"id": "14_13167654",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_13167654.jpg"
				},
				"15_13446875": {
					"id": "15_13446875",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_13446875.jpg"
				},
				"15_13447435": {
					"id": "15_13447435",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_13447435.jpg"
				},
				"16_13447436": {
					"id": "16_13447436",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_13447436.jpg"
				},
				"17_13447297": {
					"id": "17_13447297",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_13447297.jpg"
				},
				"17_13447317": {
					"id": "17_13447317",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_13447317.jpg"
				},
				"18_13447318": {
					"id": "18_13447318",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_13447318.jpg"
				},
				"2_11519582": {
					"id": "2_11519582",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_11519582.jpg"
				},
				"3_101333583": {
					"id": "3_101333583",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101333583.jpg"
				},
				"3_13447483": {
					"id": "3_13447483",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_13447483.jpg"
				},
				"5_11519585": {
					"id": "5_11519585",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_11519585.jpg"
				},
				"7_106484507": {
					"id": "7_106484507",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106484507.jpg"
				},
				"7_106484567": {
					"id": "7_106484567",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106484567.jpg"
				},
				"9_13446869": {
					"id": "9_13446869",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_13446869.jpg"
				}
			},
			"name": "Canada Goose 'MacMillan' Slim Fit Hooded Parka",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "895.00",
					"maxItemPrice": "895.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-macmillan-slim-fit-hooded-parka/4024667",
			"reviewCount": 29,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4174695": {
			"id": 4174695,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5040563",
			"colorCount": 2,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_107673679-2_104231382",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"19_107673679",
						"18_107675278",
						"1_107673681"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_107673679"
				},
				"top grey 3": {
					"id": "top grey 3",
					"label": "TOP GREY 3",
					"spriteIndex": 1,
					"mediaIds": [
						"2_104231382",
						"14_11390614",
						"12_11390612"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_104231382"
				}
			},
			"colorIds": [
				"navy",
				"top grey 3"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_11390612": {
					"id": "12_11390612",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_11390612.jpg"
				},
				"14_11390614": {
					"id": "14_11390614",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_11390614.jpg"
				},
				"18_107675278": {
					"id": "18_107675278",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107675278.jpg"
				},
				"19_107673679": {
					"id": "19_107673679",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107673679.jpg"
				},
				"1_107673681": {
					"id": "1_107673681",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107673681.jpg"
				},
				"2_104231382": {
					"id": "2_104231382",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_104231382.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "100.00",
					"maxItemPrice": "100.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-crewneck-t-shirt/4174695",
			"reviewCount": 15,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4316766": {
			"id": 4316766,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5141101",
			"colorCount": 1,
			"colorDefaultId": "black 1",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_102520710",
			"colorsById": {
				"black 1": {
					"id": "black 1",
					"label": "BLACK 1",
					"spriteIndex": 0,
					"mediaIds": [
						"10_102520710",
						"13_102520713",
						"5_102520725"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_102520710"
				}
			},
			"colorIds": [
				"black 1"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_102520710": {
					"id": "10_102520710",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_102520710.jpg"
				},
				"13_102520713": {
					"id": "13_102520713",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_102520713.jpg"
				},
				"5_102520725": {
					"id": "5_102520725",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_102520725.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Cotton Jersey Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "103.00",
					"maxItemPrice": "103.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-cotton-jersey-crewneck-t-shirt/4316766",
			"reviewCount": 43,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4392660": {
			"id": 4392660,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5197566",
			"colorCount": 7,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_106802439-17_103859397-0_103859600-5_105969105-6_103858546-12_103843912-11_103859471",
			"colorsById": {
				"admiral blue": {
					"id": "admiral blue",
					"label": "ADMIRAL BLUE",
					"spriteIndex": 1,
					"mediaIds": [
						"17_103859397",
						"2_103859402",
						"8_103858568"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "17_103859397"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"0_103859600",
						"8_103859588",
						"17_103860577"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_103859600"
				},
				"early light": {
					"id": "early light",
					"label": "EARLY LIGHT",
					"spriteIndex": 3,
					"mediaIds": [
						"5_105969105",
						"8_105969108",
						"16_105969116"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "5_105969105"
				},
				"graphite": {
					"id": "graphite",
					"label": "GRAPHITE",
					"spriteIndex": 4,
					"mediaIds": [
						"6_103858546",
						"7_103858547",
						"1_103858601"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "6_103858546"
				},
				"military green": {
					"id": "military green",
					"label": "MILITARY GREEN",
					"spriteIndex": 5,
					"mediaIds": [
						"12_103843912",
						"1_103843921",
						"17_100026437"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "12_103843912"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"19_106802439",
						"13_106802453",
						"10_106802450"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_106802439"
				},
				"red": {
					"id": "red",
					"label": "RED",
					"spriteIndex": 6,
					"mediaIds": [
						"11_103859471",
						"14_103859474",
						"9_103859549"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "11_103859471"
				}
			},
			"colorIds": [
				"navy",
				"admiral blue",
				"black",
				"early light",
				"graphite",
				"military green",
				"red"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_103859600": {
					"id": "0_103859600",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_103859600.jpg"
				},
				"10_106802450": {
					"id": "10_106802450",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106802450.jpg"
				},
				"11_103859471": {
					"id": "11_103859471",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_103859471.jpg"
				},
				"12_103843912": {
					"id": "12_103843912",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_103843912.jpg"
				},
				"13_106802453": {
					"id": "13_106802453",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106802453.jpg"
				},
				"14_103859474": {
					"id": "14_103859474",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103859474.jpg"
				},
				"16_105969116": {
					"id": "16_105969116",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105969116.jpg"
				},
				"17_100026437": {
					"id": "17_100026437",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_100026437.jpg"
				},
				"17_103859397": {
					"id": "17_103859397",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103859397.jpg"
				},
				"17_103860577": {
					"id": "17_103860577",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103860577.jpg"
				},
				"19_106802439": {
					"id": "19_106802439",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106802439.jpg"
				},
				"1_103843921": {
					"id": "1_103843921",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103843921.jpg"
				},
				"1_103858601": {
					"id": "1_103858601",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103858601.jpg"
				},
				"2_103859402": {
					"id": "2_103859402",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_103859402.jpg"
				},
				"5_105969105": {
					"id": "5_105969105",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105969105.jpg"
				},
				"6_103858546": {
					"id": "6_103858546",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_103858546.jpg"
				},
				"7_103858547": {
					"id": "7_103858547",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103858547.jpg"
				},
				"8_103858568": {
					"id": "8_103858568",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_103858568.jpg"
				},
				"8_103859588": {
					"id": "8_103859588",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_103859588.jpg"
				},
				"8_105969108": {
					"id": "8_105969108",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105969108.jpg"
				},
				"9_103859549": {
					"id": "9_103859549",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_103859549.jpg"
				}
			},
			"name": "Canada Goose Wyndham Slim Fit Genuine Coyote Fur Trim Down Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "995.00",
					"maxItemPrice": "995.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-wyndham-slim-fit-genuine-coyote-fur-trim-down-jacket/4392660",
			"reviewCount": 24,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4406814": {
			"id": 4406814,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5206326",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_12737752",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"12_12737752",
						"11_12737751",
						"14_12737734"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_12737752"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_12737751": {
					"id": "11_12737751",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_12737751.jpg"
				},
				"12_12737752": {
					"id": "12_12737752",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_12737752.jpg"
				},
				"14_12737734": {
					"id": "14_12737734",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_12737734.jpg"
				}
			},
			"name": "Peter Millar Flynn Classic Fit Solid Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "745.00",
					"maxItemPrice": "745.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-flynn-classic-fit-solid-wool-suit/4406814",
			"reviewCount": 23,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"4459330": {
			"id": 4459330,
			"brandId": 4317,
			"brandName": "ROBERT BARAKETT",
			"styleNumber": "5245053",
			"colorCount": 6,
			"colorDefaultId": "winter purple",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_107869104-7_107869027-10_101987770-4_101974184-4_101975244-6_103530266",
			"colorsById": {
				"beluga": {
					"id": "beluga",
					"label": "BELUGA",
					"spriteIndex": 1,
					"mediaIds": [
						"7_107869027",
						"4_107852464",
						"2_107182322"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "7_107869027"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"10_101987770",
						"7_100549887",
						"8_100549888"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_101987770"
				},
				"blue night": {
					"id": "blue night",
					"label": "BLUE NIGHT",
					"spriteIndex": 3,
					"mediaIds": [
						"4_101974184",
						"3_101974183",
						"3_101974403"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "4_101974184"
				},
				"iron": {
					"id": "iron",
					"label": "IRON",
					"spriteIndex": 4,
					"mediaIds": [
						"4_101975244",
						"2_101975242",
						"10_101975290"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "4_101975244"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 5,
					"mediaIds": [
						"6_103530266",
						"16_100329016",
						"4_100328924"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "6_103530266"
				},
				"winter purple": {
					"id": "winter purple",
					"label": "WINTER PURPLE",
					"spriteIndex": 0,
					"mediaIds": [
						"4_107869104",
						"19_107852459",
						"2_107182322"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "4_107869104"
				}
			},
			"colorIds": [
				"winter purple",
				"beluga",
				"black",
				"blue night",
				"iron",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_101975290": {
					"id": "10_101975290",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_101975290.jpg"
				},
				"10_101987770": {
					"id": "10_101987770",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_101987770.jpg"
				},
				"16_100329016": {
					"id": "16_100329016",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100329016.jpg"
				},
				"19_107852459": {
					"id": "19_107852459",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107852459.jpg"
				},
				"2_101975242": {
					"id": "2_101975242",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101975242.jpg"
				},
				"2_107182322": {
					"id": "2_107182322",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107182322.jpg"
				},
				"3_101974183": {
					"id": "3_101974183",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101974183.jpg"
				},
				"3_101974403": {
					"id": "3_101974403",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101974403.jpg"
				},
				"4_100328924": {
					"id": "4_100328924",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_100328924.jpg"
				},
				"4_101974184": {
					"id": "4_101974184",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101974184.jpg"
				},
				"4_101975244": {
					"id": "4_101975244",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101975244.jpg"
				},
				"4_107852464": {
					"id": "4_107852464",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107852464.jpg"
				},
				"4_107869104": {
					"id": "4_107869104",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107869104.jpg"
				},
				"6_103530266": {
					"id": "6_103530266",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_103530266.jpg"
				},
				"7_100549887": {
					"id": "7_100549887",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_100549887.jpg"
				},
				"7_107869027": {
					"id": "7_107869027",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107869027.jpg"
				},
				"8_100549888": {
					"id": "8_100549888",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_100549888.jpg"
				}
			},
			"name": "Robert Barakett Georgia Regular Fit V-Neck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/robert-barakett-georgia-regular-fit-v-neck-t-shirt/4459330",
			"reviewCount": 50,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4470526": {
			"id": 4470526,
			"brandId": 7260,
			"brandName": "TRAVISMATHEW",
			"styleNumber": "5253805",
			"colorCount": 3,
			"colorDefaultId": "heather light blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_106870993-10_101790730-8_105972988",
			"colorsById": {
				"blackberry/ white": {
					"id": "blackberry/ white",
					"label": "BLACKBERRY/ WHITE",
					"spriteIndex": 1,
					"mediaIds": [
						"10_101790730",
						"9_101790729",
						"14_101790954"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "10_101790730"
				},
				"heather black": {
					"id": "heather black",
					"label": "HEATHER BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"8_105972988",
						"11_105980731",
						"14_105972994"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_105972988"
				},
				"heather light blue": {
					"id": "heather light blue",
					"label": "HEATHER LIGHT BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_106870993",
						"16_106870996",
						"16_105931976"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_106870993"
				}
			},
			"colorIds": [
				"heather light blue",
				"blackberry/ white",
				"heather black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_101790730": {
					"id": "10_101790730",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_101790730.jpg"
				},
				"11_105980731": {
					"id": "11_105980731",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105980731.jpg"
				},
				"13_106870993": {
					"id": "13_106870993",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106870993.jpg"
				},
				"14_101790954": {
					"id": "14_101790954",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_101790954.jpg"
				},
				"14_105972994": {
					"id": "14_105972994",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105972994.jpg"
				},
				"16_105931976": {
					"id": "16_105931976",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105931976.jpg"
				},
				"16_106870996": {
					"id": "16_106870996",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106870996.jpg"
				},
				"8_105972988": {
					"id": "8_105972988",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105972988.jpg"
				},
				"9_101790729": {
					"id": "9_101790729",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101790729.jpg"
				}
			},
			"name": "TravisMathew The Zinna Regular Fit Performance Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "84.95",
					"maxItemPrice": "84.95",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/travismathew-the-zinna-regular-fit-performance-polo/4470526",
			"reviewCount": 25,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4470527": {
			"id": 4470527,
			"brandId": 7260,
			"brandName": "TRAVISMATHEW",
			"styleNumber": "5253806",
			"colorCount": 6,
			"colorDefaultId": "blue nights",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_104619309-17_102985757-3_105545343-5_101774485-3_102745023-0_102985600",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"17_102985757",
						"15_101774495",
						"0_101774520"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "17_102985757"
				},
				"blue nights": {
					"id": "blue nights",
					"label": "BLUE NIGHTS",
					"spriteIndex": 0,
					"mediaIds": [
						"9_104619309",
						"19_104619479",
						"19_104619459"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_104619309"
				},
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 2,
					"mediaIds": [
						"3_105545343",
						"11_105545891",
						"6_105545966"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_105545343"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 3,
					"mediaIds": [
						"5_101774485",
						"4_101774484",
						"9_101774489"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "5_101774485"
				},
				"light grey": {
					"id": "light grey",
					"label": "LIGHT GREY",
					"spriteIndex": 4,
					"mediaIds": [
						"3_102745023",
						"4_102744944",
						"3_102744983"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_102745023"
				},
				"vintage indigo": {
					"id": "vintage indigo",
					"label": "VINTAGE INDIGO",
					"spriteIndex": 5,
					"mediaIds": [
						"0_102985600",
						"4_101788124",
						"2_101788062"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_102985600"
				}
			},
			"colorIds": [
				"blue nights",
				"black",
				"charcoal",
				"khaki",
				"light grey",
				"vintage indigo"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_101774520": {
					"id": "0_101774520",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_101774520.jpg"
				},
				"0_102985600": {
					"id": "0_102985600",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_102985600.jpg"
				},
				"11_105545891": {
					"id": "11_105545891",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105545891.jpg"
				},
				"15_101774495": {
					"id": "15_101774495",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_101774495.jpg"
				},
				"17_102985757": {
					"id": "17_102985757",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_102985757.jpg"
				},
				"19_104619459": {
					"id": "19_104619459",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104619459.jpg"
				},
				"19_104619479": {
					"id": "19_104619479",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104619479.jpg"
				},
				"2_101788062": {
					"id": "2_101788062",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101788062.jpg"
				},
				"3_102744983": {
					"id": "3_102744983",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_102744983.jpg"
				},
				"3_102745023": {
					"id": "3_102745023",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_102745023.jpg"
				},
				"3_105545343": {
					"id": "3_105545343",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105545343.jpg"
				},
				"4_101774484": {
					"id": "4_101774484",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101774484.jpg"
				},
				"4_101788124": {
					"id": "4_101788124",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101788124.jpg"
				},
				"4_102744944": {
					"id": "4_102744944",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_102744944.jpg"
				},
				"5_101774485": {
					"id": "5_101774485",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_101774485.jpg"
				},
				"6_105545966": {
					"id": "6_105545966",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105545966.jpg"
				},
				"9_101774489": {
					"id": "9_101774489",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101774489.jpg"
				},
				"9_104619309": {
					"id": "9_104619309",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104619309.jpg"
				}
			},
			"name": "TravisMathew Beck Stretch Performance Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "84.95",
					"maxItemPrice": "84.95",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/travismathew-beck-stretch-performance-shorts/4470527",
			"reviewCount": 50,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4493952": {
			"id": 4493952,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5271720",
			"colorCount": 2,
			"colorDefaultId": "black oxide melange",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_106943608-2_103110722",
			"colorsById": {
				"black oxide melange": {
					"id": "black oxide melange",
					"label": "BLACK OXIDE MELANGE",
					"spriteIndex": 0,
					"mediaIds": [
						"8_106943608",
						"17_100735057",
						"18_100735058"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_106943608"
				},
				"grey wolf melange": {
					"id": "grey wolf melange",
					"label": "GREY WOLF MELANGE",
					"spriteIndex": 1,
					"mediaIds": [
						"2_103110722",
						"7_103110727",
						"12_103110852"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_103110722"
				}
			},
			"colorIds": [
				"black oxide melange",
				"grey wolf melange"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_103110852": {
					"id": "12_103110852",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_103110852.jpg"
				},
				"17_100735057": {
					"id": "17_100735057",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_100735057.jpg"
				},
				"18_100735058": {
					"id": "18_100735058",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_100735058.jpg"
				},
				"2_103110722": {
					"id": "2_103110722",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_103110722.jpg"
				},
				"7_103110727": {
					"id": "7_103110727",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103110727.jpg"
				},
				"8_106943608": {
					"id": "8_106943608",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106943608.jpg"
				}
			},
			"name": "Zella Pyrite Knit Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "49.00",
					"maxItemPrice": "49.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-pyrite-knit-shorts/4493952",
			"reviewCount": 65,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4509445": {
			"id": 4509445,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5284251",
			"colorCount": 4,
			"colorDefaultId": "graphite",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_101797541-2_100278762-18_102140298-6_101797186",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"2_100278762",
						"14_100278254",
						"8_100278208"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "2_100278762"
				},
				"graphite": {
					"id": "graphite",
					"label": "GRAPHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"1_101797541",
						"8_101797808",
						"6_101797846"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "1_101797541"
				},
				"military green": {
					"id": "military green",
					"label": "MILITARY GREEN",
					"spriteIndex": 2,
					"mediaIds": [
						"18_102140298",
						"3_102140303",
						"2_102140302"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "18_102140298"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"6_101797186",
						"0_101797760",
						"4_101797844"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_101797186"
				}
			},
			"colorIds": [
				"graphite",
				"black",
				"military green",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_101797760": {
					"id": "0_101797760",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_101797760.jpg"
				},
				"14_100278254": {
					"id": "14_100278254",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100278254.jpg"
				},
				"18_102140298": {
					"id": "18_102140298",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102140298.jpg"
				},
				"1_101797541": {
					"id": "1_101797541",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_101797541.jpg"
				},
				"2_100278762": {
					"id": "2_100278762",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_100278762.jpg"
				},
				"2_102140302": {
					"id": "2_102140302",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_102140302.jpg"
				},
				"3_102140303": {
					"id": "3_102140303",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_102140303.jpg"
				},
				"4_101797844": {
					"id": "4_101797844",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101797844.jpg"
				},
				"6_101797186": {
					"id": "6_101797186",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_101797186.jpg"
				},
				"6_101797846": {
					"id": "6_101797846",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_101797846.jpg"
				},
				"8_100278208": {
					"id": "8_100278208",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_100278208.jpg"
				},
				"8_101797808": {
					"id": "8_101797808",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_101797808.jpg"
				}
			},
			"name": "Canada Goose Emory Slim Fit Genuine Coyote Fur Trim Parka",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,095.00",
					"maxItemPrice": "1,095.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-emory-slim-fit-genuine-coyote-fur-trim-parka/4509445",
			"reviewCount": 17,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"4527527": {
			"id": 4527527,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5297228",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_100385802",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"2_100385802",
						"7_100385627",
						"8_100385628"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_100385802"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"2_100385802": {
					"id": "2_100385802",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_100385802.jpg"
				},
				"7_100385627": {
					"id": "7_100385627",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_100385627.jpg"
				},
				"8_100385628": {
					"id": "8_100385628",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_100385628.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Twin Hearts Slim Fit Jersey T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-twin-hearts-slim-fit-jersey-t-shirt/4527527",
			"reviewCount": 22,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4540390": {
			"id": 4540390,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5306269",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_101818558",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"18_101818558",
						"14_100495854",
						"16_100495856"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "18_101818558"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_100495854": {
					"id": "14_100495854",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100495854.jpg"
				},
				"16_100495856": {
					"id": "16_100495856",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100495856.jpg"
				},
				"18_101818558": {
					"id": "18_101818558",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_101818558.jpg"
				}
			},
			"name": "AG Tellis SUD Modern Slim Fit Stretch Twill Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "188.00",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-tellis-sud-modern-slim-fit-stretch-twill-pants/4540390",
			"reviewCount": 72,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4543316": {
			"id": 4543316,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5308419",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_100216888",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"8_100216888",
						"19_100216879",
						"0_100216880"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_100216888"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_100216880": {
					"id": "0_100216880",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_100216880.jpg"
				},
				"19_100216879": {
					"id": "19_100216879",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_100216879.jpg"
				},
				"8_100216888": {
					"id": "8_100216888",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_100216888.jpg"
				}
			},
			"name": "Ted Baker London Josh Trim Fit Wool & Mohair Tuxedo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,098.00",
					"maxItemPrice": "1,098.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-josh-trim-fit-wool-mohair-tuxedo/4543316",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"4593721": {
			"id": 4593721,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5342541",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_101231689-14_100966174",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"9_101231689",
						"9_104600769",
						"6_101231706"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_101231689"
				},
				"perfect navy": {
					"id": "perfect navy",
					"label": "PERFECT NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"14_100966174",
						"19_100954339",
						"19_100954239"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_100966174"
				}
			},
			"colorIds": [
				"black",
				"perfect navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_100966174": {
					"id": "14_100966174",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100966174.jpg"
				},
				"19_100954239": {
					"id": "19_100954239",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_100954239.jpg"
				},
				"19_100954339": {
					"id": "19_100954339",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_100954339.jpg"
				},
				"6_101231706": {
					"id": "6_101231706",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_101231706.jpg"
				},
				"9_101231689": {
					"id": "9_101231689",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101231689.jpg"
				},
				"9_104600769": {
					"id": "9_104600769",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104600769.jpg"
				}
			},
			"name": "Peter Millar Zip Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "150.00",
					"maxItemPrice": "150.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-zip-jacket/4593721",
			"reviewCount": 24,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4602756": {
			"id": 4602756,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5349965",
			"colorCount": 3,
			"colorDefaultId": "stone",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_104354250-5_103061705-17_103059457",
			"colorsById": {
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 1,
					"mediaIds": [
						"5_103061705",
						"7_101227147",
						"16_101227176"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "5_103061705"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 2,
					"mediaIds": [
						"17_103059457",
						"11_101227051",
						"12_101227052"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "17_103059457"
				},
				"stone": {
					"id": "stone",
					"label": "STONE",
					"spriteIndex": 0,
					"mediaIds": [
						"10_104354250",
						"11_104354251",
						"13_101221453"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "10_104354250"
				}
			},
			"colorIds": [
				"stone",
				"khaki",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_104354250": {
					"id": "10_104354250",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_104354250.jpg"
				},
				"11_101227051": {
					"id": "11_101227051",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_101227051.jpg"
				},
				"11_104354251": {
					"id": "11_104354251",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_104354251.jpg"
				},
				"12_101227052": {
					"id": "12_101227052",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_101227052.jpg"
				},
				"13_101221453": {
					"id": "13_101221453",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_101221453.jpg"
				},
				"16_101227176": {
					"id": "16_101227176",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_101227176.jpg"
				},
				"17_103059457": {
					"id": "17_103059457",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103059457.jpg"
				},
				"5_103061705": {
					"id": "5_103061705",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_103061705.jpg"
				},
				"7_101227147": {
					"id": "7_101227147",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_101227147.jpg"
				}
			},
			"name": "Peter Millar Crown Vintage Canvas Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "158.00",
					"maxItemPrice": "158.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "63.20",
					"maxItemPrice": "63.20",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-crown-vintage-canvas-pants/4602756",
			"reviewCount": 26,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"4616604": {
			"id": 4616604,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5359890",
			"colorCount": 3,
			"colorDefaultId": "stormy sand",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_107661906-14_107597854-6_102207246",
			"colorsById": {
				"blue heron": {
					"id": "blue heron",
					"label": "BLUE HERON",
					"spriteIndex": 1,
					"mediaIds": [
						"14_107597854",
						"12_107628372",
						"10_107628370"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_107597854"
				},
				"stormy sand": {
					"id": "stormy sand",
					"label": "STORMY SAND",
					"spriteIndex": 0,
					"mediaIds": [
						"6_107661906",
						"5_107661905",
						"4_107661904"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "6_107661906"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 2,
					"mediaIds": [
						"6_102207246",
						"1_102207241",
						"14_102207334"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "6_102207246"
				}
			},
			"colorIds": [
				"stormy sand",
				"blue heron",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107628370": {
					"id": "10_107628370",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107628370.jpg"
				},
				"12_107628372": {
					"id": "12_107628372",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107628372.jpg"
				},
				"14_102207334": {
					"id": "14_102207334",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_102207334.jpg"
				},
				"14_107597854": {
					"id": "14_107597854",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107597854.jpg"
				},
				"1_102207241": {
					"id": "1_102207241",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_102207241.jpg"
				},
				"4_107661904": {
					"id": "4_107661904",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107661904.jpg"
				},
				"5_107661905": {
					"id": "5_107661905",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107661905.jpg"
				},
				"6_102207246": {
					"id": "6_102207246",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_102207246.jpg"
				},
				"6_107661906": {
					"id": "6_107661906",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107661906.jpg"
				}
			},
			"name": "AG Everett SUD Slim Straight Fit Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "188.00",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 30,
					"minItemPrice": "131.60",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-everett-sud-slim-straight-fit-pants/4616604",
			"reviewCount": 176,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4624146": {
			"id": 4624146,
			"brandId": 173,
			"brandName": "COLE HAAN",
			"styleNumber": "5366347",
			"colorCount": 3,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_103324581-18_106019378-12_106019372",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"18_106019378",
						"9_106017929",
						"7_106017927"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_106019378"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"1_103324581",
						"2_103324582",
						"13_103324593"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_103324581"
				},
				"tan": {
					"id": "tan",
					"label": "TAN",
					"spriteIndex": 2,
					"mediaIds": [
						"12_106019372",
						"10_106018490",
						"8_106018488"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "12_106019372"
				}
			},
			"colorIds": [
				"navy",
				"black",
				"tan"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106018490": {
					"id": "10_106018490",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106018490.jpg"
				},
				"12_106019372": {
					"id": "12_106019372",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106019372.jpg"
				},
				"13_103324593": {
					"id": "13_103324593",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_103324593.jpg"
				},
				"18_106019378": {
					"id": "18_106019378",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106019378.jpg"
				},
				"1_103324581": {
					"id": "1_103324581",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103324581.jpg"
				},
				"2_103324582": {
					"id": "2_103324582",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_103324582.jpg"
				},
				"7_106017927": {
					"id": "7_106017927",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106017927.jpg"
				},
				"8_106018488": {
					"id": "8_106018488",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106018488.jpg"
				},
				"9_106017929": {
					"id": "9_106017929",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106017929.jpg"
				}
			},
			"name": "Cole Haan Signature Water Resistant Car Coat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "265.00",
					"maxItemPrice": "265.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cole-haan-signature-water-resistant-car-coat/4624146",
			"reviewCount": 4,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4626607": {
			"id": 4626607,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5368366",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_101164549",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"9_101164549",
						"8_101164548",
						"15_101164575"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_101164549"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_101164575": {
					"id": "15_101164575",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_101164575.jpg"
				},
				"8_101164548": {
					"id": "8_101164548",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_101164548.jpg"
				},
				"9_101164549": {
					"id": "9_101164549",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101164549.jpg"
				}
			},
			"name": "Peter Millar Flynn Classic Fit Wool Blazer",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "545.00",
					"maxItemPrice": "545.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "327.00",
					"maxItemPrice": "327.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-flynn-classic-fit-wool-blazer/4626607",
			"reviewCount": 13,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4629861": {
			"id": 4629861,
			"brandId": 168,
			"brandName": "Cutter & Buck",
			"styleNumber": "5371132",
			"colorCount": 2,
			"colorDefaultId": "charcoal heather",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_100874095-15_100874175",
			"colorsById": {
				"charcoal heather": {
					"id": "charcoal heather",
					"label": "CHARCOAL HEATHER",
					"spriteIndex": 0,
					"mediaIds": [
						"15_100874095",
						"14_100874094",
						"7_100874287"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "15_100874095"
				},
				"liberty navy": {
					"id": "liberty navy",
					"label": "LIBERTY NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"15_100874175",
						"14_100874174",
						"3_100874063"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_100874175"
				}
			},
			"colorIds": [
				"charcoal heather",
				"liberty navy"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_100874094": {
					"id": "14_100874094",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100874094.jpg"
				},
				"14_100874174": {
					"id": "14_100874174",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100874174.jpg"
				},
				"15_100874095": {
					"id": "15_100874095",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_100874095.jpg"
				},
				"15_100874175": {
					"id": "15_100874175",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_100874175.jpg"
				},
				"19_105807139": {
					"id": "19_105807139",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105807139.jpg"
				},
				"19_105807159": {
					"id": "19_105807159",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105807159.jpg"
				},
				"3_100874063": {
					"id": "3_100874063",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_100874063.jpg"
				},
				"7_100874287": {
					"id": "7_100874287",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_100874287.jpg"
				}
			},
			"name": "Cutter & Buck Lakemont Half Zip Sweater",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "110.00",
					"maxItemPrice": "110.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "55.00",
					"maxItemPrice": "55.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cutter-buck-lakemont-half-zip-sweater/4629861",
			"reviewCount": 19,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4636661": {
			"id": 4636661,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5376588",
			"colorCount": 2,
			"colorDefaultId": "water mist",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_107559910-14_106539574",
			"colorsById": {
				"midnight berlin": {
					"id": "midnight berlin",
					"label": "MIDNIGHT BERLIN",
					"spriteIndex": 1,
					"mediaIds": [
						"14_106539574",
						"13_106589173",
						"1_106539581"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_106539574"
				},
				"water mist": {
					"id": "water mist",
					"label": "WATER MIST",
					"spriteIndex": 0,
					"mediaIds": [
						"10_107559910",
						"11_107559911",
						"5_102491405"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_107559910"
				}
			},
			"colorIds": [
				"water mist",
				"midnight berlin"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107559910": {
					"id": "10_107559910",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107559910.jpg"
				},
				"11_107559911": {
					"id": "11_107559911",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107559911.jpg"
				},
				"13_106589173": {
					"id": "13_106589173",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106589173.jpg"
				},
				"14_106539574": {
					"id": "14_106539574",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106539574.jpg"
				},
				"1_106539581": {
					"id": "1_106539581",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106539581.jpg"
				},
				"5_102491405": {
					"id": "5_102491405",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_102491405.jpg"
				}
			},
			"name": "AG Wanderer Modern Slim Fit Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "125.00",
					"maxItemPrice": "125.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-wanderer-modern-slim-fit-shorts/4636661",
			"reviewCount": 72,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4698559": {
			"id": 4698559,
			"brandId": 1354,
			"brandName": "DAVID DONAHUE",
			"styleNumber": "5420317",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_102155631",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"11_102155631",
						"16_102155616",
						"10_102155630"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "11_102155631"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_102155630": {
					"id": "10_102155630",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_102155630.jpg"
				},
				"11_102155631": {
					"id": "11_102155631",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_102155631.jpg"
				},
				"16_102155616": {
					"id": "16_102155616",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_102155616.jpg"
				}
			},
			"name": "David Donahue Trim Fit Solid Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "145.00",
					"maxItemPrice": "145.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/david-donahue-trim-fit-solid-dress-shirt/4698559",
			"reviewCount": 9,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"4705933": {
			"id": 4705933,
			"brandId": 7862,
			"brandName": "KSUBI",
			"styleNumber": "5426188",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_103137377",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"17_103137377",
						"0_103137380",
						"16_103137496"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "17_103137377"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_103137380": {
					"id": "0_103137380",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_103137380.jpg"
				},
				"16_103137496": {
					"id": "16_103137496",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103137496.jpg"
				},
				"17_103137377": {
					"id": "17_103137377",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103137377.jpg"
				}
			},
			"name": "Ksubi Chitch Boneyard Skinny Fit Jeans",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "240.00",
					"maxItemPrice": "240.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ksubi-chitch-boneyard-skinny-fit-jeans/4705933",
			"reviewCount": 2,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4721877": {
			"id": 4721877,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5438620",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_101459171-0_101459160",
			"colorsById": {
				"airforce": {
					"id": "airforce",
					"label": "AIRFORCE",
					"spriteIndex": 1,
					"mediaIds": [
						"0_101459160",
						"19_101459159",
						"19_101537299"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_101459160"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_101459171",
						"8_101459168",
						"11_101537711"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "11_101459171"
				}
			},
			"colorIds": [
				"black",
				"airforce"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_101459160": {
					"id": "0_101459160",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_101459160.jpg"
				},
				"11_101459171": {
					"id": "11_101459171",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_101459171.jpg"
				},
				"11_101537711": {
					"id": "11_101537711",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_101537711.jpg"
				},
				"19_101459159": {
					"id": "19_101459159",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_101459159.jpg"
				},
				"19_101537299": {
					"id": "19_101537299",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_101537299.jpg"
				},
				"8_101459168": {
					"id": "8_101459168",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_101459168.jpg"
				}
			},
			"name": "Calvin Klein 3-Pack Comfort Microfiber Trunks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "44.50",
					"maxItemPrice": "44.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 14,
					"maxItemPercentOff": 20,
					"minItemPrice": "35.60",
					"maxItemPrice": "38.23",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-3-pack-comfort-microfiber-trunks/4721877",
			"reviewCount": 75,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"4721879": {
			"id": 4721879,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5438619",
			"colorCount": 1,
			"colorDefaultId": "airforce",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_101459157",
			"colorsById": {
				"airforce": {
					"id": "airforce",
					"label": "AIRFORCE",
					"spriteIndex": 0,
					"mediaIds": [
						"17_101459157",
						"7_101459127",
						"12_101537592"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "17_101459157"
				}
			},
			"colorIds": [
				"airforce"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_101537592": {
					"id": "12_101537592",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_101537592.jpg"
				},
				"17_101459157": {
					"id": "17_101459157",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_101459157.jpg"
				},
				"7_101459127": {
					"id": "7_101459127",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_101459127.jpg"
				}
			},
			"name": "Calvin Klein 3-Pack Comfort Microfiber Boxer Briefs",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "44.50",
					"maxItemPrice": "44.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-3-pack-comfort-microfiber-boxer-briefs/4721879",
			"reviewCount": 67,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4736932": {
			"id": 4736932,
			"brandId": 4886,
			"brandName": "HURLEY",
			"styleNumber": "5451060",
			"colorCount": 3,
			"colorDefaultId": "obsidian",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_103394284-15_101959095-5_101958985",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"15_101959095",
						"14_101959094",
						"9_101959329"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "15_101959095"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 2,
					"mediaIds": [
						"5_101958985",
						"4_101958984",
						"7_101959067"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "5_101958985"
				},
				"obsidian": {
					"id": "obsidian",
					"label": "OBSIDIAN",
					"spriteIndex": 0,
					"mediaIds": [
						"4_103394284",
						"8_103394788",
						"1_103394641"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_103394284"
				}
			},
			"colorIds": [
				"obsidian",
				"black",
				"khaki"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_101959094": {
					"id": "14_101959094",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_101959094.jpg"
				},
				"15_101959095": {
					"id": "15_101959095",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_101959095.jpg"
				},
				"1_103394641": {
					"id": "1_103394641",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103394641.jpg"
				},
				"4_101958984": {
					"id": "4_101958984",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101958984.jpg"
				},
				"4_103394284": {
					"id": "4_103394284",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_103394284.jpg"
				},
				"5_101958985": {
					"id": "5_101958985",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_101958985.jpg"
				},
				"7_101959067": {
					"id": "7_101959067",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_101959067.jpg"
				},
				"8_103394788": {
					"id": "8_103394788",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_103394788.jpg"
				},
				"9_101959329": {
					"id": "9_101959329",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_101959329.jpg"
				}
			},
			"name": "Hurley Dri-FIT Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "60.00",
					"maxItemPrice": "60.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/hurley-dri-fit-shorts/4736932",
			"reviewCount": 102,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4742302": {
			"id": 4742302,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5455709",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_101621436-7_101848907",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"16_101621436",
						"0_101622260",
						"5_101682605"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "16_101621436"
				},
				"blue multi": {
					"id": "blue multi",
					"label": "BLUE MULTI",
					"spriteIndex": 1,
					"mediaIds": [
						"7_101848907",
						"4_101848904",
						"0_102068260"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_101848907"
				}
			},
			"colorIds": [
				"black",
				"blue multi"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_101622260": {
					"id": "0_101622260",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_101622260.jpg"
				},
				"0_102068260": {
					"id": "0_102068260",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_102068260.jpg"
				},
				"16_101621436": {
					"id": "16_101621436",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_101621436.jpg"
				},
				"4_101848904": {
					"id": "4_101848904",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101848904.jpg"
				},
				"5_101682605": {
					"id": "5_101682605",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_101682605.jpg"
				},
				"7_101848907": {
					"id": "7_101848907",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_101848907.jpg"
				}
			},
			"name": "Calvin Klein Steel Micro 3-Pack Boxer Briefs",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-steel-micro-3-pack-boxer-briefs/4742302",
			"reviewCount": 81,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4759609": {
			"id": 4759609,
			"brandId": 1114,
			"brandName": "EMPORIO ARMANI",
			"styleNumber": "5470381",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_102620572",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"12_102620572",
						"12_102620672",
						"14_102620614"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_102620572"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_102620572": {
					"id": "12_102620572",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_102620572.jpg"
				},
				"12_102620672": {
					"id": "12_102620672",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_102620672.jpg"
				},
				"14_102620614": {
					"id": "14_102620614",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_102620614.jpg"
				}
			},
			"name": "Emporio Armani Trim Fit Wool Tuxedo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,795.00",
					"maxItemPrice": "1,795.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "1,077.00",
					"maxItemPrice": "1,077.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/emporio-armani-trim-fit-wool-tuxedo/4759609",
			"reviewCount": 2,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"4766280": {
			"id": 4766280,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5475179",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_103157511",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_103157511",
						"16_103157516",
						"7_102162927"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "11_103157511"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_103157511": {
					"id": "11_103157511",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_103157511.jpg"
				},
				"16_103157516": {
					"id": "16_103157516",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103157516.jpg"
				},
				"7_102162927": {
					"id": "7_102162927",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_102162927.jpg"
				}
			},
			"name": "Ted Baker London Jay Trim Fit Solid Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "798.00",
					"maxItemPrice": "798.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-jay-trim-fit-solid-wool-suit/4766280",
			"reviewCount": 20,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"4788223": {
			"id": 4788223,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5492687",
			"colorCount": 1,
			"colorDefaultId": "grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_102485453",
			"colorsById": {
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"13_102485453",
						"18_102485458",
						"3_102485583"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "13_102485453"
				}
			},
			"colorIds": [
				"grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_102485453": {
					"id": "13_102485453",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_102485453.jpg"
				},
				"18_102485458": {
					"id": "18_102485458",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102485458.jpg"
				},
				"3_102485583": {
					"id": "3_102485583",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_102485583.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Red Heart Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "304.00",
					"maxItemPrice": "304.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-red-heart-hoodie/4788223",
			"reviewCount": 5,
			"reviewStarRating": 3,
			"storeAvailability": null
		},
		"4795271": {
			"id": 4795271,
			"brandId": 16393,
			"brandName": "CHAMPION",
			"styleNumber": "5498521",
			"colorCount": 4,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_102865728-3_105575943-6_102355526-3_106854823",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"3_105575943",
						"7_101882387",
						"12_101882452"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "3_105575943"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"8_102865728",
						"10_102865730",
						"1_102865661"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_102865728"
				},
				"oxford grey": {
					"id": "oxford grey",
					"label": "OXFORD GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"6_102355526",
						"18_102355698",
						"5_102355705"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "6_102355526"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 3,
					"mediaIds": [
						"3_106854823",
						"4_101879144",
						"17_101879137"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "3_106854823"
				}
			},
			"colorIds": [
				"navy",
				"black",
				"oxford grey",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_102865730": {
					"id": "10_102865730",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_102865730.jpg"
				},
				"12_101882452": {
					"id": "12_101882452",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_101882452.jpg"
				},
				"17_101879137": {
					"id": "17_101879137",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_101879137.jpg"
				},
				"18_102355698": {
					"id": "18_102355698",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102355698.jpg"
				},
				"1_102865661": {
					"id": "1_102865661",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_102865661.jpg"
				},
				"3_105575943": {
					"id": "3_105575943",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105575943.jpg"
				},
				"3_106854823": {
					"id": "3_106854823",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106854823.jpg"
				},
				"4_101879144": {
					"id": "4_101879144",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_101879144.jpg"
				},
				"5_102355705": {
					"id": "5_102355705",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_102355705.jpg"
				},
				"6_102355526": {
					"id": "6_102355526",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_102355526.jpg"
				},
				"7_101882387": {
					"id": "7_101882387",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_101882387.jpg"
				},
				"8_102865728": {
					"id": "8_102865728",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_102865728.jpg"
				}
			},
			"name": "Champion Reverse Weave® Pullover Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "50.00",
					"maxItemPrice": "50.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/champion-reverse-weave-pullover-hoodie/4795271",
			"reviewCount": 362,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4806425": {
			"id": 4806425,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5507382",
			"colorCount": 4,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107423212-12_107423092-1_105147621-10_107423190",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107423212",
						"15_107426175",
						"8_102295828"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_107423212"
				},
				"heather charcoal": {
					"id": "heather charcoal",
					"label": "HEATHER CHARCOAL",
					"spriteIndex": 1,
					"mediaIds": [
						"12_107423092",
						"5_102403965",
						"19_102404579"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "12_107423092"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"1_105147621",
						"3_105147623",
						"19_105147619"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "1_105147621"
				},
				"heather navy": {
					"id": "heather navy",
					"label": "HEATHER NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"10_107423190",
						"18_103323878",
						"18_103324958"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_107423190"
				}
			},
			"colorIds": [
				"black",
				"heather charcoal",
				"heather grey",
				"heather navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107423190": {
					"id": "10_107423190",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107423190.jpg"
				},
				"12_107423092": {
					"id": "12_107423092",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107423092.jpg"
				},
				"12_107423212": {
					"id": "12_107423212",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107423212.jpg"
				},
				"15_107426175": {
					"id": "15_107426175",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107426175.jpg"
				},
				"18_103323878": {
					"id": "18_103323878",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103323878.jpg"
				},
				"18_103324958": {
					"id": "18_103324958",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103324958.jpg"
				},
				"19_102404579": {
					"id": "19_102404579",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_102404579.jpg"
				},
				"19_105147619": {
					"id": "19_105147619",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105147619.jpg"
				},
				"1_105147621": {
					"id": "1_105147621",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105147621.jpg"
				},
				"3_105147623": {
					"id": "3_105147623",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105147623.jpg"
				},
				"5_102403965": {
					"id": "5_102403965",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_102403965.jpg"
				},
				"8_102295828": {
					"id": "8_102295828",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_102295828.jpg"
				}
			},
			"name": "Vuori Ponto Jogger Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "84.00",
					"maxItemPrice": "84.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-ponto-jogger-pants/4806425",
			"reviewCount": 13,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4806426": {
			"id": 4806426,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5507383",
			"colorCount": 9,
			"colorDefaultId": "grey linen text digi",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107839838-12_102248952-18_107195598-12_102248912-4_107846624-5_107546785-14_107274874-7_107581247-2_107839822",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"12_102248952",
						"11_102248951",
						"16_102248956"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_102248952"
				},
				"black watercolor camo": {
					"id": "black watercolor camo",
					"label": "BLACK WATERCOLOR CAMO",
					"spriteIndex": 2,
					"mediaIds": [
						"18_107195598",
						"16_107195636",
						"15_107195635"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_107195598"
				},
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 3,
					"mediaIds": [
						"12_102248912",
						"19_102249139",
						"13_102249113"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "12_102248912"
				},
				"cloud": {
					"id": "cloud",
					"label": "CLOUD",
					"spriteIndex": 4,
					"mediaIds": [
						"4_107846624",
						"13_107814613",
						"11_107581251"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_107846624"
				},
				"grey linen text digi": {
					"id": "grey linen text digi",
					"label": "GREY LINEN TEXT DIGI",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107839838",
						"2_107839842",
						"11_107581251"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_107839838"
				},
				"indigo": {
					"id": "indigo",
					"label": "INDIGO",
					"spriteIndex": 5,
					"mediaIds": [
						"5_107546785",
						"6_107546786",
						"11_107581251"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107546785"
				},
				"palm grey stripe": {
					"id": "palm grey stripe",
					"label": "PALM GREY STRIPE",
					"spriteIndex": 6,
					"mediaIds": [
						"14_107274874",
						"3_107301743",
						"1_107301741"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "14_107274874"
				},
				"patina watercolor camo": {
					"id": "patina watercolor camo",
					"label": "PATINA WATERCOLOR CAMO",
					"spriteIndex": 7,
					"mediaIds": [
						"7_107581247",
						"12_107581252",
						"11_107581251"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_107581247"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 8,
					"mediaIds": [
						"2_107839822",
						"3_107826963",
						"11_107581251"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "2_107839822"
				}
			},
			"colorIds": [
				"grey linen text digi",
				"black",
				"black watercolor camo",
				"charcoal",
				"cloud",
				"indigo",
				"palm grey stripe",
				"patina watercolor camo",
				"white"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_102248951": {
					"id": "11_102248951",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_102248951.jpg"
				},
				"11_107581251": {
					"id": "11_107581251",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107581251.jpg"
				},
				"12_102248912": {
					"id": "12_102248912",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_102248912.jpg"
				},
				"12_102248952": {
					"id": "12_102248952",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_102248952.jpg"
				},
				"12_107581252": {
					"id": "12_107581252",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107581252.jpg"
				},
				"13_102249113": {
					"id": "13_102249113",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_102249113.jpg"
				},
				"13_107814613": {
					"id": "13_107814613",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107814613.jpg"
				},
				"14_107274874": {
					"id": "14_107274874",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107274874.jpg"
				},
				"15_107195635": {
					"id": "15_107195635",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107195635.jpg"
				},
				"16_102248956": {
					"id": "16_102248956",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_102248956.jpg"
				},
				"16_107195636": {
					"id": "16_107195636",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107195636.jpg"
				},
				"18_107195598": {
					"id": "18_107195598",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107195598.jpg"
				},
				"18_107839838": {
					"id": "18_107839838",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107839838.jpg"
				},
				"19_102249139": {
					"id": "19_102249139",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_102249139.jpg"
				},
				"1_107301741": {
					"id": "1_107301741",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107301741.jpg"
				},
				"2_107839822": {
					"id": "2_107839822",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107839822.jpg"
				},
				"2_107839842": {
					"id": "2_107839842",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107839842.jpg"
				},
				"3_107301743": {
					"id": "3_107301743",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107301743.jpg"
				},
				"3_107826963": {
					"id": "3_107826963",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107826963.jpg"
				},
				"4_107846624": {
					"id": "4_107846624",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107846624.jpg"
				},
				"5_107546785": {
					"id": "5_107546785",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107546785.jpg"
				},
				"6_107546786": {
					"id": "6_107546786",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107546786.jpg"
				},
				"7_107581247": {
					"id": "7_107581247",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107581247.jpg"
				}
			},
			"name": "vuori Kore Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "68.00",
					"maxItemPrice": "68.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-kore-shorts/4806426",
			"reviewCount": 7,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"4806427": {
			"id": 4806427,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5507384",
			"colorCount": 6,
			"colorDefaultId": "copper heather",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_107839957-13_107841493-16_102401216-0_102401340-2_107203162-16_105665076",
			"colorsById": {
				"cloud heather": {
					"id": "cloud heather",
					"label": "CLOUD HEATHER",
					"spriteIndex": 1,
					"mediaIds": [
						"13_107841493",
						"14_107808774",
						"10_107202050"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_107841493"
				},
				"copper heather": {
					"id": "copper heather",
					"label": "COPPER HEATHER",
					"spriteIndex": 0,
					"mediaIds": [
						"17_107839957",
						"17_107839977",
						"10_107202050"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "17_107839957"
				},
				"heather charcoal": {
					"id": "heather charcoal",
					"label": "HEATHER CHARCOAL",
					"spriteIndex": 2,
					"mediaIds": [
						"16_102401216",
						"18_102401238",
						"0_102401060"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "16_102401216"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 3,
					"mediaIds": [
						"0_102401340",
						"15_102401335",
						"2_102401002"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "0_102401340"
				},
				"palm heather": {
					"id": "palm heather",
					"label": "PALM HEATHER",
					"spriteIndex": 4,
					"mediaIds": [
						"2_107203162",
						"10_107203170",
						"10_107202050"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "2_107203162"
				},
				"salt heather": {
					"id": "salt heather",
					"label": "SALT HEATHER",
					"spriteIndex": 5,
					"mediaIds": [
						"16_105665076",
						"16_105665136",
						"11_105665091"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "16_105665076"
				}
			},
			"colorIds": [
				"copper heather",
				"cloud heather",
				"heather charcoal",
				"heather grey",
				"palm heather",
				"salt heather"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_102401060": {
					"id": "0_102401060",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_102401060.jpg"
				},
				"0_102401340": {
					"id": "0_102401340",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_102401340.jpg"
				},
				"10_107202050": {
					"id": "10_107202050",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107202050.jpg"
				},
				"10_107203170": {
					"id": "10_107203170",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107203170.jpg"
				},
				"11_105665091": {
					"id": "11_105665091",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105665091.jpg"
				},
				"13_107841493": {
					"id": "13_107841493",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107841493.jpg"
				},
				"14_107808774": {
					"id": "14_107808774",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107808774.jpg"
				},
				"15_102401335": {
					"id": "15_102401335",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_102401335.jpg"
				},
				"16_102401216": {
					"id": "16_102401216",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_102401216.jpg"
				},
				"16_105665076": {
					"id": "16_105665076",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105665076.jpg"
				},
				"16_105665136": {
					"id": "16_105665136",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105665136.jpg"
				},
				"17_107839957": {
					"id": "17_107839957",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107839957.jpg"
				},
				"17_107839977": {
					"id": "17_107839977",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107839977.jpg"
				},
				"18_102401238": {
					"id": "18_102401238",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102401238.jpg"
				},
				"2_102401002": {
					"id": "2_102401002",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_102401002.jpg"
				},
				"2_107203162": {
					"id": "2_107203162",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107203162.jpg"
				}
			},
			"name": "vuori Strato Slim Fit Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "44.00",
					"maxItemPrice": "44.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-strato-slim-fit-crewneck-t-shirt/4806427",
			"reviewCount": 10,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"4860563": {
			"id": 4860563,
			"brandId": 16393,
			"brandName": "CHAMPION",
			"styleNumber": "5546438",
			"colorCount": 1,
			"colorDefaultId": "citrus pink",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_107081762",
			"colorsById": {
				"citrus pink": {
					"id": "citrus pink",
					"label": "CITRUS PINK",
					"spriteIndex": 0,
					"mediaIds": [
						"2_107081762",
						"3_107081763",
						"7_102995767"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "2_107081762"
				}
			},
			"colorIds": [
				"citrus pink"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"2_107081762": {
					"id": "2_107081762",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107081762.jpg"
				},
				"3_107081763": {
					"id": "3_107081763",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107081763.jpg"
				},
				"7_102995767": {
					"id": "7_102995767",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_102995767.jpg"
				}
			},
			"name": "Champion Reverse Weave® Crew Sweatshirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "50.00",
					"maxItemPrice": "50.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/champion-reverse-weave-crew-sweatshirt/4860563",
			"reviewCount": 151,
			"reviewStarRating": 4.2,
			"storeAvailability": null
		},
		"4876730": {
			"id": 4876730,
			"brandId": 320,
			"brandName": "BOSS HUGO BOSS",
			"styleNumber": "5559123",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_103581847-6_103428106",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"7_103581847",
						"12_103581852",
						"1_103581761"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "7_103581847"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"6_103428106",
						"14_103428434",
						"19_103428419"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_103428106"
				}
			},
			"colorIds": [
				"black",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_103581852": {
					"id": "12_103581852",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_103581852.jpg"
				},
				"14_103428434": {
					"id": "14_103428434",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103428434.jpg"
				},
				"19_103428419": {
					"id": "19_103428419",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_103428419.jpg"
				},
				"1_103581761": {
					"id": "1_103581761",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_103581761.jpg"
				},
				"6_103428106": {
					"id": "6_103428106",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_103428106.jpg"
				},
				"7_103581847": {
					"id": "7_103581847",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103581847.jpg"
				}
			},
			"name": "BOSS Halven/Gentry Slim Fit Wool Tuxedo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "995.00",
					"maxItemPrice": "995.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 40,
					"minItemPrice": "597.00",
					"maxItemPrice": "995.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/boss-halven-gentry-slim-fit-wool-tuxedo/4876730",
			"reviewCount": 7,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"4919923": {
			"id": 4919923,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5593768",
			"colorCount": 1,
			"colorDefaultId": "light grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_103747035",
			"colorsById": {
				"light grey": {
					"id": "light grey",
					"label": "LIGHT GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"15_103747035",
						"7_104743747",
						"6_103752766"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "15_103747035"
				}
			},
			"colorIds": [
				"light grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_103747035": {
					"id": "15_103747035",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_103747035.jpg"
				},
				"6_103752766": {
					"id": "6_103752766",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_103752766.jpg"
				},
				"7_104743747": {
					"id": "7_104743747",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104743747.jpg"
				}
			},
			"name": "Ted Baker London Jay Trim Fit Solid Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "798.00",
					"maxItemPrice": "798.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 55,
					"minItemPrice": "359.10",
					"maxItemPrice": "798.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-jay-trim-fit-solid-wool-suit/4919923",
			"reviewCount": 8,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"4930689": {
			"id": 4930689,
			"brandId": 8111,
			"brandName": "BONOBOS",
			"styleNumber": "5600840",
			"colorCount": 4,
			"colorDefaultId": "monument",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_105618794-14_107685094-14_107589254-4_107608304",
			"colorsById": {
				"dark surf": {
					"id": "dark surf",
					"label": "DARK SURF",
					"spriteIndex": 1,
					"mediaIds": [
						"14_107685094",
						"13_107691433",
						"10_107691430"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_107685094"
				},
				"monument": {
					"id": "monument",
					"label": "MONUMENT",
					"spriteIndex": 0,
					"mediaIds": [
						"14_105618794",
						"6_105626466",
						"18_105626618"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "14_105618794"
				},
				"quayside grey": {
					"id": "quayside grey",
					"label": "QUAYSIDE GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"14_107589254",
						"19_107627659",
						"10_107627650"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "14_107589254"
				},
				"sandpoint": {
					"id": "sandpoint",
					"label": "SANDPOINT",
					"spriteIndex": 3,
					"mediaIds": [
						"4_107608304",
						"11_107627671",
						"4_107627664"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "4_107608304"
				}
			},
			"colorIds": [
				"monument",
				"dark surf",
				"quayside grey",
				"sandpoint"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107627650": {
					"id": "10_107627650",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107627650.jpg"
				},
				"10_107691430": {
					"id": "10_107691430",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107691430.jpg"
				},
				"11_107627671": {
					"id": "11_107627671",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107627671.jpg"
				},
				"13_107691433": {
					"id": "13_107691433",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107691433.jpg"
				},
				"14_105618794": {
					"id": "14_105618794",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105618794.jpg"
				},
				"14_107589254": {
					"id": "14_107589254",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107589254.jpg"
				},
				"14_107685094": {
					"id": "14_107685094",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107685094.jpg"
				},
				"18_105626618": {
					"id": "18_105626618",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105626618.jpg"
				},
				"19_107627659": {
					"id": "19_107627659",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107627659.jpg"
				},
				"4_107608304": {
					"id": "4_107608304",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107608304.jpg"
				},
				"4_107627664": {
					"id": "4_107627664",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107627664.jpg"
				},
				"6_105626466": {
					"id": "6_105626466",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105626466.jpg"
				}
			},
			"name": "Bonobos Summer Weight Slim Fit Stretch Chinos",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bonobos-summer-weight-slim-fit-stretch-chinos/4930689",
			"reviewCount": 40,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4961810": {
			"id": 4961810,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5625491",
			"colorCount": 3,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_105889298-2_107559702-11_107559711",
			"colorsById": {
				"british grey": {
					"id": "british grey",
					"label": "BRITISH GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"2_107559702",
						"5_107611785",
						"8_107559708"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_107559702"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"18_105889298",
						"17_106024257",
						"2_105889302"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_105889298"
				},
				"stone": {
					"id": "stone",
					"label": "STONE",
					"spriteIndex": 2,
					"mediaIds": [
						"11_107559711",
						"16_107559716",
						"15_107559715"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "11_107559711"
				}
			},
			"colorIds": [
				"navy",
				"british grey",
				"stone"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107559711": {
					"id": "11_107559711",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107559711.jpg"
				},
				"15_107559715": {
					"id": "15_107559715",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107559715.jpg"
				},
				"16_107559716": {
					"id": "16_107559716",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107559716.jpg"
				},
				"17_106024257": {
					"id": "17_106024257",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106024257.jpg"
				},
				"18_105889298": {
					"id": "18_105889298",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105889298.jpg"
				},
				"2_105889302": {
					"id": "2_105889302",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105889302.jpg"
				},
				"2_107559702": {
					"id": "2_107559702",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107559702.jpg"
				},
				"5_107611785": {
					"id": "5_107611785",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107611785.jpg"
				},
				"8_107559708": {
					"id": "8_107559708",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107559708.jpg"
				}
			},
			"name": "Peter Millar Five-Pocket Performance Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "149.00",
					"maxItemPrice": "149.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-five-pocket-performance-pants/4961810",
			"reviewCount": 190,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"4964534": {
			"id": 4964534,
			"brandId": 18457,
			"brandName": "BOMBAS",
			"styleNumber": "5627818",
			"colorCount": 3,
			"colorDefaultId": "black/ cream/ grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_103337796-15_105007515-4_106776884",
			"colorsById": {
				"black/ cream/ grey": {
					"id": "black/ cream/ grey",
					"label": "BLACK/ CREAM/ GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"16_103337796",
						"17_103337797",
						"5_103337805"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "16_103337796"
				},
				"blue multi": {
					"id": "blue multi",
					"label": "BLUE MULTI",
					"spriteIndex": 1,
					"mediaIds": [
						"15_105007515",
						"3_105007523",
						"5_103337805"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_105007515"
				},
				"midnight/ soft blue/ grey": {
					"id": "midnight/ soft blue/ grey",
					"label": "MIDNIGHT/ SOFT BLUE/ GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"4_106776884",
						"3_103337803",
						"7_103337807"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "4_106776884"
				}
			},
			"colorIds": [
				"black/ cream/ grey",
				"blue multi",
				"midnight/ soft blue/ grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_105007515": {
					"id": "15_105007515",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105007515.jpg"
				},
				"16_103337796": {
					"id": "16_103337796",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103337796.jpg"
				},
				"17_103337797": {
					"id": "17_103337797",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103337797.jpg"
				},
				"3_103337803": {
					"id": "3_103337803",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_103337803.jpg"
				},
				"3_105007523": {
					"id": "3_105007523",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105007523.jpg"
				},
				"4_106776884": {
					"id": "4_106776884",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106776884.jpg"
				},
				"5_103337805": {
					"id": "5_103337805",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_103337805.jpg"
				},
				"7_103337807": {
					"id": "7_103337807",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103337807.jpg"
				}
			},
			"name": "Bombas Colorblock Ankle Socks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "12.00",
					"maxItemPrice": "12.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bombas-colorblock-ankle-socks/4964534",
			"reviewCount": 14,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"4984963": {
			"id": 4984963,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "5643022",
			"colorCount": 1,
			"colorDefaultId": "jet black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_106930553",
			"colorsById": {
				"jet black": {
					"id": "jet black",
					"label": "JET BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"13_106930553",
						"16_106930556",
						"13_103981413"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_106930553"
				}
			},
			"colorIds": [
				"jet black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_103981413": {
					"id": "13_103981413",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_103981413.jpg"
				},
				"13_106930553": {
					"id": "13_106930553",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106930553.jpg"
				},
				"16_106930556": {
					"id": "16_106930556",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106930556.jpg"
				}
			},
			"name": "ALLSAINTS Cora Leather Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "498.00",
					"maxItemPrice": "498.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-cora-leather-jacket/4984963",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"4990632": {
			"id": 4990632,
			"brandId": 8111,
			"brandName": "BONOBOS",
			"styleNumber": "5647316",
			"colorCount": 6,
			"colorDefaultId": "micro stripe navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_105996106-16_106983716-6_105559666-8_105249028-12_107608492-19_105248839",
			"colorsById": {
				"blue/grey": {
					"id": "blue/grey",
					"label": "BLUE/GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"16_106983716",
						"6_106985346",
						"11_106985331"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_106983716"
				},
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"6_105559666",
						"12_105578532",
						"11_105578531"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "6_105559666"
				},
				"khaki tan": {
					"id": "khaki tan",
					"label": "KHAKI TAN",
					"spriteIndex": 3,
					"mediaIds": [
						"8_105249028",
						"17_104555937",
						"4_104554084"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "8_105249028"
				},
				"micro stripe navy": {
					"id": "micro stripe navy",
					"label": "MICRO STRIPE NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"6_105996106",
						"10_105992010",
						"9_105992009"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_105996106"
				},
				"mushroom": {
					"id": "mushroom",
					"label": "MUSHROOM",
					"spriteIndex": 4,
					"mediaIds": [
						"12_107608492",
						"8_107627728",
						"4_107627704"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "12_107608492"
				},
				"wednesday tan": {
					"id": "wednesday tan",
					"label": "WEDNESDAY TAN",
					"spriteIndex": 5,
					"mediaIds": [
						"19_105248839",
						"7_105248827",
						"7_105248847"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "19_105248839"
				}
			},
			"colorIds": [
				"micro stripe navy",
				"blue/grey",
				"grey",
				"khaki tan",
				"mushroom",
				"wednesday tan"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_105992010": {
					"id": "10_105992010",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_105992010.jpg"
				},
				"11_105578531": {
					"id": "11_105578531",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105578531.jpg"
				},
				"11_106985331": {
					"id": "11_106985331",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106985331.jpg"
				},
				"12_105578532": {
					"id": "12_105578532",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105578532.jpg"
				},
				"12_107608492": {
					"id": "12_107608492",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107608492.jpg"
				},
				"16_106983716": {
					"id": "16_106983716",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106983716.jpg"
				},
				"17_104555937": {
					"id": "17_104555937",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_104555937.jpg"
				},
				"19_105248839": {
					"id": "19_105248839",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105248839.jpg"
				},
				"4_104554084": {
					"id": "4_104554084",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_104554084.jpg"
				},
				"4_107627704": {
					"id": "4_107627704",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107627704.jpg"
				},
				"6_105559666": {
					"id": "6_105559666",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105559666.jpg"
				},
				"6_105996106": {
					"id": "6_105996106",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105996106.jpg"
				},
				"6_106985346": {
					"id": "6_106985346",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106985346.jpg"
				},
				"7_105248827": {
					"id": "7_105248827",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105248827.jpg"
				},
				"7_105248847": {
					"id": "7_105248847",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105248847.jpg"
				},
				"8_105249028": {
					"id": "8_105249028",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105249028.jpg"
				},
				"8_107627728": {
					"id": "8_107627728",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107627728.jpg"
				},
				"9_105992009": {
					"id": "9_105992009",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_105992009.jpg"
				}
			},
			"name": "Bonobos Stretch Weekday Warrior Slim Fit Dress Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 59,
					"minItemPrice": "39.99",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bonobos-stretch-weekday-warrior-slim-fit-dress-pants/4990632",
			"reviewCount": 64,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5023278": {
			"id": 5023278,
			"brandId": 6832,
			"brandName": "TOMMY JOHN",
			"styleNumber": "560089_2",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_7771556",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"16_7771556",
						"11_12158371",
						"16_12155056"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "16_7771556"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_12158371": {
					"id": "11_12158371",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_12158371.jpg"
				},
				"16_12155056": {
					"id": "16_12155056",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_12155056.jpg"
				},
				"16_7771556": {
					"id": "16_7771556",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_7771556.jpg"
				}
			},
			"name": "Tommy John Cool Cotton Crewneck Undershirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "40.00",
					"maxItemPrice": "40.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/tommy-john-cool-cotton-crewneck-undershirt/5023278",
			"reviewCount": 23,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5041719": {
			"id": 5041719,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5681668",
			"colorCount": 2,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_104819455-3_104819443",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"3_104819443",
						"6_104819446",
						"14_104819394"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "3_104819443"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"15_104819455",
						"0_104819460",
						"19_104819419"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "15_104819455"
				}
			},
			"colorIds": [
				"white",
				"black"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_104819460": {
					"id": "0_104819460",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_104819460.jpg"
				},
				"14_104819394": {
					"id": "14_104819394",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104819394.jpg"
				},
				"15_104819455": {
					"id": "15_104819455",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104819455.jpg"
				},
				"19_104819419": {
					"id": "19_104819419",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104819419.jpg"
				},
				"3_104819443": {
					"id": "3_104819443",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_104819443.jpg"
				},
				"6_104819446": {
					"id": "6_104819446",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_104819446.jpg"
				}
			},
			"name": "Calvin Klein Ultrasoft Stretch Modal Solid Tank",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "32.00",
					"maxItemPrice": "32.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "22.40",
					"maxItemPrice": "22.40",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-ultrasoft-stretch-modal-solid-tank/5041719",
			"reviewCount": 9,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5041726": {
			"id": 5041726,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5681669",
			"colorCount": 3,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_104819432-11_104819371-9_104819349",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"11_104819371",
						"12_104819372",
						"18_104819338"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "11_104819371"
				},
				"grey heather": {
					"id": "grey heather",
					"label": "GREY HEATHER",
					"spriteIndex": 2,
					"mediaIds": [
						"9_104819349",
						"12_104819352",
						"4_104819284"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_104819349"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"12_104819432",
						"15_104819435",
						"13_104819413"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "12_104819432"
				}
			},
			"colorIds": [
				"white",
				"black",
				"grey heather"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_104819371": {
					"id": "11_104819371",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_104819371.jpg"
				},
				"12_104819352": {
					"id": "12_104819352",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_104819352.jpg"
				},
				"12_104819372": {
					"id": "12_104819372",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_104819372.jpg"
				},
				"12_104819432": {
					"id": "12_104819432",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_104819432.jpg"
				},
				"13_104819413": {
					"id": "13_104819413",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104819413.jpg"
				},
				"15_104819435": {
					"id": "15_104819435",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104819435.jpg"
				},
				"18_104819338": {
					"id": "18_104819338",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_104819338.jpg"
				},
				"4_104819284": {
					"id": "4_104819284",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_104819284.jpg"
				},
				"9_104819349": {
					"id": "9_104819349",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104819349.jpg"
				}
			},
			"name": "Calvin Klein Ultrasoft Modal Blend Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.00",
					"maxItemPrice": "34.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "23.80",
					"maxItemPrice": "23.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-ultrasoft-modal-blend-crewneck-t-shirt/5041726",
			"reviewCount": 44,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5082001": {
			"id": 5082001,
			"brandId": 7398,
			"brandName": "STANCE",
			"styleNumber": "5713502",
			"colorCount": 1,
			"colorDefaultId": "black/ white/ grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_105224408",
			"colorsById": {
				"black/ white/ grey": {
					"id": "black/ white/ grey",
					"label": "BLACK/ WHITE/ GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"8_105224408",
						"16_105224416",
						"12_105224412"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_105224408"
				}
			},
			"colorIds": [
				"black/ white/ grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_105224412": {
					"id": "12_105224412",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105224412.jpg"
				},
				"16_105224416": {
					"id": "16_105224416",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105224416.jpg"
				},
				"8_105224408": {
					"id": "8_105224408",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105224408.jpg"
				}
			},
			"name": "Stance Gamut 3-Pack No-Show Socks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "25.00",
					"maxItemPrice": "25.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/stance-gamut-3-pack-no-show-socks/5082001",
			"reviewCount": 6,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5084856": {
			"id": 5084856,
			"brandId": 320,
			"brandName": "BOSS HUGO BOSS",
			"styleNumber": "5715722",
			"colorCount": 3,
			"colorDefaultId": "blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_104997862-9_104335669-5_104574365",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"9_104335669",
						"1_104335661",
						"2_104335702"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_104335669"
				},
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"2_104997862",
						"10_104997870",
						"16_104997956"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_104997862"
				},
				"dark grey": {
					"id": "dark grey",
					"label": "DARK GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"5_104574365",
						"19_104574379",
						"18_104574378"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_104574365"
				}
			},
			"colorIds": [
				"blue",
				"black",
				"dark grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_104997870": {
					"id": "10_104997870",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_104997870.jpg"
				},
				"16_104997956": {
					"id": "16_104997956",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_104997956.jpg"
				},
				"18_104574378": {
					"id": "18_104574378",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_104574378.jpg"
				},
				"19_104574379": {
					"id": "19_104574379",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104574379.jpg"
				},
				"1_104335661": {
					"id": "1_104335661",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_104335661.jpg"
				},
				"2_104335702": {
					"id": "2_104335702",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_104335702.jpg"
				},
				"2_104997862": {
					"id": "2_104997862",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_104997862.jpg"
				},
				"5_104574365": {
					"id": "5_104574365",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_104574365.jpg"
				},
				"9_104335669": {
					"id": "9_104335669",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104335669.jpg"
				}
			},
			"name": "BOSS Huge/Genius Trim Fit Solid Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "895.00",
					"maxItemPrice": "895.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/boss-huge-genius-trim-fit-solid-wool-suit/5084856",
			"reviewCount": 16,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5110490": {
			"id": 5110490,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5734185",
			"colorCount": 3,
			"colorDefaultId": "blue vivid end on end",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107711061-4_107711084-13_107717833",
			"colorsById": {
				"blue vivid end on end": {
					"id": "blue vivid end on end",
					"label": "BLUE VIVID END ON END",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107711061",
						"9_107717809",
						"4_105407224"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_107711061"
				},
				"navy blazer end on end": {
					"id": "navy blazer end on end",
					"label": "NAVY BLAZER END ON END",
					"spriteIndex": 1,
					"mediaIds": [
						"4_107711084",
						"10_107698250",
						"4_105407224"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_107711084"
				},
				"pink compact end on end": {
					"id": "pink compact end on end",
					"label": "PINK COMPACT END ON END",
					"spriteIndex": 2,
					"mediaIds": [
						"13_107717833",
						"18_107700378",
						"4_105407224"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "13_107717833"
				}
			},
			"colorIds": [
				"blue vivid end on end",
				"navy blazer end on end",
				"pink compact end on end"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107698250": {
					"id": "10_107698250",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107698250.jpg"
				},
				"13_107717833": {
					"id": "13_107717833",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107717833.jpg"
				},
				"18_107700378": {
					"id": "18_107700378",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107700378.jpg"
				},
				"1_107711061": {
					"id": "1_107711061",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107711061.jpg"
				},
				"4_105407224": {
					"id": "4_105407224",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105407224.jpg"
				},
				"4_107711084": {
					"id": "4_107711084",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107711084.jpg"
				},
				"9_107717809": {
					"id": "9_107717809",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107717809.jpg"
				}
			},
			"name": "1901 Linen Slim Fit Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "29.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-linen-slim-fit-shirt/5110490",
			"reviewCount": 15,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"5113113": {
			"id": 5113113,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5736531",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_104896519",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"19_104896519",
						"10_104898810",
						"13_104891853"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_104896519"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_104898810": {
					"id": "10_104898810",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_104898810.jpg"
				},
				"13_104891853": {
					"id": "13_104891853",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104891853.jpg"
				},
				"19_104896519": {
					"id": "19_104896519",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104896519.jpg"
				}
			},
			"name": "Peter Millar Sean Regular Fit Stretch Jersey Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "89.00",
					"maxItemPrice": "89.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-sean-regular-fit-stretch-jersey-polo/5113113",
			"reviewCount": 49,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5116651": {
			"id": 5116651,
			"brandId": 7862,
			"brandName": "KSUBI",
			"styleNumber": "5739626",
			"colorCount": 1,
			"colorDefaultId": "blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_104393593",
			"colorsById": {
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_104393593",
						"11_104727451",
						"7_104393587"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_104393593"
				}
			},
			"colorIds": [
				"blue"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_104727451": {
					"id": "11_104727451",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_104727451.jpg"
				},
				"13_104393593": {
					"id": "13_104393593",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104393593.jpg"
				},
				"7_104393587": {
					"id": "7_104393587",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104393587.jpg"
				}
			},
			"name": "Ksubi Oh G Oversize Denim Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "220.00",
					"maxItemPrice": "220.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 24,
					"maxItemPercentOff": 24,
					"minItemPrice": "168.00",
					"maxItemPrice": "168.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ksubi-oh-g-oversize-denim-jacket/5116651",
			"reviewCount": 3,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5158095": {
			"id": 5158095,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5768911",
			"colorCount": 7,
			"colorDefaultId": "red",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_104849230-2_106953642-9_104850449-7_104850487-1_106003581-0_106003600-4_107152404",
			"colorsById": {
				"admiral navy": {
					"id": "admiral navy",
					"label": "ADMIRAL NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"2_106953642",
						"19_106954659",
						"5_106953645"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_106953642"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"9_104850449",
						"14_104850474",
						"14_104846454"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_104850449"
				},
				"lichen": {
					"id": "lichen",
					"label": "LICHEN",
					"spriteIndex": 3,
					"mediaIds": [
						"7_104850487",
						"1_104850481",
						"18_104846458"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "7_104850487"
				},
				"military green": {
					"id": "military green",
					"label": "MILITARY GREEN",
					"spriteIndex": 4,
					"mediaIds": [
						"1_106003581",
						"15_106003575",
						"8_106003588"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "1_106003581"
				},
				"northern night": {
					"id": "northern night",
					"label": "NORTHERN NIGHT",
					"spriteIndex": 5,
					"mediaIds": [
						"0_106003600",
						"0_106003640",
						"17_106003637"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_106003600"
				},
				"red": {
					"id": "red",
					"label": "RED",
					"spriteIndex": 0,
					"mediaIds": [
						"10_104849230",
						"8_104849388",
						"7_104846647"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "10_104849230"
				},
				"tempest blue": {
					"id": "tempest blue",
					"label": "TEMPEST BLUE",
					"spriteIndex": 6,
					"mediaIds": [
						"4_107152404",
						"0_106954680",
						"6_107152386"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_107152404"
				}
			},
			"colorIds": [
				"red",
				"admiral navy",
				"black",
				"lichen",
				"military green",
				"northern night",
				"tempest blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106003600": {
					"id": "0_106003600",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106003600.jpg"
				},
				"0_106003640": {
					"id": "0_106003640",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106003640.jpg"
				},
				"0_106954680": {
					"id": "0_106954680",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106954680.jpg"
				},
				"10_104849230": {
					"id": "10_104849230",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_104849230.jpg"
				},
				"14_104846454": {
					"id": "14_104846454",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104846454.jpg"
				},
				"14_104850474": {
					"id": "14_104850474",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104850474.jpg"
				},
				"15_106003575": {
					"id": "15_106003575",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106003575.jpg"
				},
				"17_106003637": {
					"id": "17_106003637",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106003637.jpg"
				},
				"18_104846458": {
					"id": "18_104846458",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_104846458.jpg"
				},
				"19_106954659": {
					"id": "19_106954659",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106954659.jpg"
				},
				"1_104850481": {
					"id": "1_104850481",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_104850481.jpg"
				},
				"1_106003581": {
					"id": "1_106003581",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106003581.jpg"
				},
				"2_106953642": {
					"id": "2_106953642",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106953642.jpg"
				},
				"4_107152404": {
					"id": "4_107152404",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107152404.jpg"
				},
				"5_106953645": {
					"id": "5_106953645",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106953645.jpg"
				},
				"6_107152386": {
					"id": "6_107152386",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107152386.jpg"
				},
				"7_104846647": {
					"id": "7_104846647",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104846647.jpg"
				},
				"7_104850487": {
					"id": "7_104850487",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104850487.jpg"
				},
				"8_104849388": {
					"id": "8_104849388",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_104849388.jpg"
				},
				"8_106003588": {
					"id": "8_106003588",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106003588.jpg"
				},
				"9_104850449": {
					"id": "9_104850449",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104850449.jpg"
				}
			},
			"name": "Canada Goose Cabri Hooded Packable Down Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "625.00",
					"maxItemPrice": "625.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-cabri-hooded-packable-down-jacket/5158095",
			"reviewCount": 7,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5158096": {
			"id": 5158096,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5768912",
			"colorCount": 5,
			"colorDefaultId": "tempest blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_107378730-19_106987579-13_104850453-1_106275741-5_107049245",
			"colorsById": {
				"admiral navy": {
					"id": "admiral navy",
					"label": "ADMIRAL NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"19_106987579",
						"5_106987625",
						"10_106987590"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_106987579"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"13_104850453",
						"19_104850479",
						"15_104846255"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_104850453"
				},
				"northern night": {
					"id": "northern night",
					"label": "NORTHERN NIGHT",
					"spriteIndex": 3,
					"mediaIds": [
						"1_106275741",
						"8_106275828",
						"6_106275806"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_106275741"
				},
				"red": {
					"id": "red",
					"label": "RED",
					"spriteIndex": 4,
					"mediaIds": [
						"5_107049245",
						"5_107049265",
						"4_107049264"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "5_107049245"
				},
				"tempest blue": {
					"id": "tempest blue",
					"label": "TEMPEST BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"10_107378730",
						"9_107378769",
						"15_107378735"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_107378730"
				}
			},
			"colorIds": [
				"tempest blue",
				"admiral navy",
				"black",
				"northern night",
				"red"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106987590": {
					"id": "10_106987590",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106987590.jpg"
				},
				"10_107378730": {
					"id": "10_107378730",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107378730.jpg"
				},
				"13_104850453": {
					"id": "13_104850453",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_104850453.jpg"
				},
				"15_104846255": {
					"id": "15_104846255",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104846255.jpg"
				},
				"15_107378735": {
					"id": "15_107378735",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107378735.jpg"
				},
				"19_104850479": {
					"id": "19_104850479",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_104850479.jpg"
				},
				"19_106987579": {
					"id": "19_106987579",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106987579.jpg"
				},
				"1_106275741": {
					"id": "1_106275741",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106275741.jpg"
				},
				"4_107049264": {
					"id": "4_107049264",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107049264.jpg"
				},
				"5_106987625": {
					"id": "5_106987625",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106987625.jpg"
				},
				"5_107049245": {
					"id": "5_107049245",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107049245.jpg"
				},
				"5_107049265": {
					"id": "5_107049265",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107049265.jpg"
				},
				"6_106275806": {
					"id": "6_106275806",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106275806.jpg"
				},
				"8_106275828": {
					"id": "8_106275828",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106275828.jpg"
				},
				"9_107378769": {
					"id": "9_107378769",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107378769.jpg"
				}
			},
			"name": "Canada Goose Dunham Slim Fit Packable Down Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "550.00",
					"maxItemPrice": "550.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-dunham-slim-fit-packable-down-jacket/5158096",
			"reviewCount": 7,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5164048": {
			"id": 5164048,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5772262",
			"colorCount": 1,
			"colorDefaultId": "equation",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_104637809",
			"colorsById": {
				"equation": {
					"id": "equation",
					"label": "EQUATION",
					"spriteIndex": 0,
					"mediaIds": [
						"9_104637809",
						"11_104637811"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_104637809"
				}
			},
			"colorIds": [
				"equation"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_104637811": {
					"id": "11_104637811",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_104637811.jpg"
				},
				"9_104637809": {
					"id": "9_104637809",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104637809.jpg"
				}
			},
			"name": "AG Everett Slim Straight Leg Jeans (Equation)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "198.00",
					"maxItemPrice": "198.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "99.00",
					"maxItemPrice": "99.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-everett-slim-straight-leg-jeans-equation/5164048",
			"reviewCount": 5,
			"reviewStarRating": 4.2,
			"storeAvailability": null
		},
		"5175520": {
			"id": 5175520,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5779450",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_105419326",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"6_105419326",
						"18_105432718",
						"15_105432895"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "6_105419326"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_105432895": {
					"id": "15_105432895",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105432895.jpg"
				},
				"18_105432718": {
					"id": "18_105432718",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105432718.jpg"
				},
				"6_105419326": {
					"id": "6_105419326",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105419326.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Logo Long Sleeve Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "132.00",
					"maxItemPrice": "132.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-logo-long-sleeve-graphic-tee/5175520",
			"reviewCount": 1,
			"reviewStarRating": 1,
			"storeAvailability": null
		},
		"5178560": {
			"id": 5178560,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5781120",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_105595820-9_106964809",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"0_105595820",
						"8_105601028",
						"8_105600968"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_105595820"
				},
				"grey wolf melange": {
					"id": "grey wolf melange",
					"label": "GREY WOLF MELANGE",
					"spriteIndex": 1,
					"mediaIds": [
						"9_106964809",
						"2_106965162",
						"12_106964992"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_106964809"
				}
			},
			"colorIds": [
				"black",
				"grey wolf melange"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_105595820": {
					"id": "0_105595820",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105595820.jpg"
				},
				"12_106964992": {
					"id": "12_106964992",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106964992.jpg"
				},
				"2_106965162": {
					"id": "2_106965162",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106965162.jpg"
				},
				"8_105600968": {
					"id": "8_105600968",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105600968.jpg"
				},
				"8_105601028": {
					"id": "8_105601028",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105601028.jpg"
				},
				"9_106964809": {
					"id": "9_106964809",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106964809.jpg"
				}
			},
			"name": "Zella Pyrite Slim Fit Jogger Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.00",
					"maxItemPrice": "59.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-pyrite-slim-fit-jogger-pants/5178560",
			"reviewCount": 64,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5196505": {
			"id": 5196505,
			"brandId": 1354,
			"brandName": "DAVID DONAHUE",
			"styleNumber": "5791272",
			"colorCount": 1,
			"colorDefaultId": "black/ white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=3_105983523",
			"colorsById": {
				"black/ white": {
					"id": "black/ white",
					"label": "BLACK/ WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"3_105983523",
						"8_105983528",
						"3_105983403"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "3_105983523"
				}
			},
			"colorIds": [
				"black/ white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"3_105983403": {
					"id": "3_105983403",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105983403.jpg"
				},
				"3_105983523": {
					"id": "3_105983523",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_105983523.jpg"
				},
				"8_105983528": {
					"id": "8_105983528",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105983528.jpg"
				}
			},
			"name": "David Donahue Regular Fit Solid Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "145.00",
					"maxItemPrice": "145.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 62,
					"maxItemPercentOff": 62,
					"minItemPrice": "54.98",
					"maxItemPrice": "54.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/david-donahue-regular-fit-solid-dress-shirt/5196505",
			"reviewCount": 4,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5218994": {
			"id": 5218994,
			"brandId": 12792,
			"brandName": "GOOD MAN BRAND",
			"styleNumber": "5805750",
			"colorCount": 3,
			"colorDefaultId": "sky captain",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_107760131-5_107760125-14_106272314",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"5_107760125",
						"18_105171438",
						"17_105171497"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "5_107760125"
				},
				"magnet": {
					"id": "magnet",
					"label": "MAGNET",
					"spriteIndex": 2,
					"mediaIds": [
						"14_106272314",
						"19_106272319",
						"7_106272307"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "14_106272314"
				},
				"sky captain": {
					"id": "sky captain",
					"label": "SKY CAPTAIN",
					"spriteIndex": 0,
					"mediaIds": [
						"11_107760131",
						"12_107760132",
						"13_105171533"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_107760131"
				}
			},
			"colorIds": [
				"sky captain",
				"black",
				"magnet"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107760131": {
					"id": "11_107760131",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107760131.jpg"
				},
				"12_107760132": {
					"id": "12_107760132",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107760132.jpg"
				},
				"13_105171533": {
					"id": "13_105171533",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_105171533.jpg"
				},
				"14_106272314": {
					"id": "14_106272314",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106272314.jpg"
				},
				"17_105171497": {
					"id": "17_105171497",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105171497.jpg"
				},
				"18_105171438": {
					"id": "18_105171438",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105171438.jpg"
				},
				"19_106272319": {
					"id": "19_106272319",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106272319.jpg"
				},
				"5_107760125": {
					"id": "5_107760125",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107760125.jpg"
				},
				"7_106272307": {
					"id": "7_106272307",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106272307.jpg"
				}
			},
			"name": "Good Man Brand Pro Slim Fit Jogger Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "128.00",
					"maxItemPrice": "128.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/good-man-brand-pro-slim-fit-jogger-pants/5218994",
			"reviewCount": 5,
			"reviewStarRating": 4.2,
			"storeAvailability": null
		},
		"5227013": {
			"id": 5227013,
			"brandId": 11669,
			"brandName": "MADEWELL",
			"styleNumber": "5771771",
			"colorCount": 1,
			"colorDefaultId": "cargo green",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_105176458",
			"colorsById": {
				"cargo green": {
					"id": "cargo green",
					"label": "CARGO GREEN",
					"spriteIndex": 0,
					"mediaIds": [
						"18_105176458",
						"18_105035638",
						"17_105035637"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "18_105176458"
				}
			},
			"colorIds": [
				"cargo green"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"17_105035637": {
					"id": "17_105035637",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105035637.jpg"
				},
				"18_105035638": {
					"id": "18_105035638",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105035638.jpg"
				},
				"18_105176458": {
					"id": "18_105176458",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105176458.jpg"
				}
			},
			"name": "Madewell Slim Fit Field Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "148.00",
					"maxItemPrice": "148.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/madewell-slim-fit-field-jacket/5227013",
			"reviewCount": 8,
			"reviewStarRating": 3.5,
			"storeAvailability": null
		},
		"5232431": {
			"id": 5232431,
			"brandId": 304,
			"brandName": "HART SCHAFFNER MARX",
			"styleNumber": "5815055",
			"colorCount": 2,
			"colorDefaultId": "grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_105133054-7_105132447",
			"colorsById": {
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"14_105133054",
						"1_105133061",
						"15_105132535"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "14_105133054"
				},
				"light blue": {
					"id": "light blue",
					"label": "LIGHT BLUE",
					"spriteIndex": 1,
					"mediaIds": [
						"7_105132447",
						"7_105132667",
						"19_105133219"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_105132447"
				}
			},
			"colorIds": [
				"grey",
				"light blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_105133054": {
					"id": "14_105133054",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105133054.jpg"
				},
				"15_105132535": {
					"id": "15_105132535",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105132535.jpg"
				},
				"19_105133219": {
					"id": "19_105133219",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105133219.jpg"
				},
				"1_105133061": {
					"id": "1_105133061",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105133061.jpg"
				},
				"7_105132447": {
					"id": "7_105132447",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105132447.jpg"
				},
				"7_105132667": {
					"id": "7_105132667",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105132667.jpg"
				}
			},
			"name": "Hart Schaffner Marx New York Classic Fit Plaid Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "695.00",
					"maxItemPrice": "895.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 55,
					"maxItemPercentOff": 55,
					"minItemPrice": "312.75",
					"maxItemPrice": "402.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/hart-schaffner-marx-new-york-classic-fit-plaid-wool-suit/5232431",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5239157": {
			"id": 5239157,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5820216",
			"colorCount": 5,
			"colorDefaultId": "charcoal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_105154038-18_105154378-9_107384909-16_107545976-8_106392708",
			"colorsById": {
				"army": {
					"id": "army",
					"label": "ARMY",
					"spriteIndex": 1,
					"mediaIds": [
						"18_105154378",
						"1_105154381",
						"1_105154441"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "18_105154378"
				},
				"black camo": {
					"id": "black camo",
					"label": "BLACK CAMO",
					"spriteIndex": 2,
					"mediaIds": [
						"9_107384909",
						"1_107385101",
						"14_107385114"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_107384909"
				},
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 0,
					"mediaIds": [
						"18_105154038",
						"4_105154044",
						"14_105154114"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_105154038"
				},
				"indigo": {
					"id": "indigo",
					"label": "INDIGO",
					"spriteIndex": 3,
					"mediaIds": [
						"16_107545976",
						"18_107545978",
						"11_107545971"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_107545976"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 4,
					"mediaIds": [
						"8_106392708",
						"3_106412263",
						"18_106412258"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "8_106392708"
				}
			},
			"colorIds": [
				"charcoal",
				"army",
				"black camo",
				"indigo",
				"khaki"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107545971": {
					"id": "11_107545971",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107545971.jpg"
				},
				"14_105154114": {
					"id": "14_105154114",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105154114.jpg"
				},
				"14_107385114": {
					"id": "14_107385114",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107385114.jpg"
				},
				"16_107545976": {
					"id": "16_107545976",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107545976.jpg"
				},
				"18_105154038": {
					"id": "18_105154038",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105154038.jpg"
				},
				"18_105154378": {
					"id": "18_105154378",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105154378.jpg"
				},
				"18_106412258": {
					"id": "18_106412258",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106412258.jpg"
				},
				"18_107545978": {
					"id": "18_107545978",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107545978.jpg"
				},
				"1_105154381": {
					"id": "1_105154381",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105154381.jpg"
				},
				"1_105154441": {
					"id": "1_105154441",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105154441.jpg"
				},
				"1_107385101": {
					"id": "1_107385101",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107385101.jpg"
				},
				"3_106412263": {
					"id": "3_106412263",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106412263.jpg"
				},
				"4_105154044": {
					"id": "4_105154044",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105154044.jpg"
				},
				"8_106392708": {
					"id": "8_106392708",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106392708.jpg"
				},
				"9_107384909": {
					"id": "9_107384909",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107384909.jpg"
				}
			},
			"name": "vuori Ripstop Slim Fit Climber Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "89.00",
					"maxItemPrice": "89.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-ripstop-slim-fit-climber-pants/5239157",
			"reviewCount": 7,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5241711": {
			"id": 5241711,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5822082",
			"colorCount": 4,
			"colorDefaultId": "tan plaza",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_107597428-14_105716694-4_105697044-7_106778067",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_105716694",
						"15_105717555",
						"2_105717582"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_105716694"
				},
				"grey obsidian heather": {
					"id": "grey obsidian heather",
					"label": "GREY OBSIDIAN HEATHER",
					"spriteIndex": 2,
					"mediaIds": [
						"4_105697044",
						"4_105717564",
						"1_105717541"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "4_105697044"
				},
				"navy halite": {
					"id": "navy halite",
					"label": "NAVY HALITE",
					"spriteIndex": 3,
					"mediaIds": [
						"7_106778067",
						"7_106778127",
						"5_106778085"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_106778067"
				},
				"tan plaza": {
					"id": "tan plaza",
					"label": "TAN PLAZA",
					"spriteIndex": 0,
					"mediaIds": [
						"8_107597428",
						"10_107597430",
						"9_107597429"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "8_107597428"
				}
			},
			"colorIds": [
				"tan plaza",
				"black",
				"grey obsidian heather",
				"navy halite"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107597430": {
					"id": "10_107597430",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107597430.jpg"
				},
				"14_105716694": {
					"id": "14_105716694",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105716694.jpg"
				},
				"15_105717555": {
					"id": "15_105717555",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105717555.jpg"
				},
				"1_105717541": {
					"id": "1_105717541",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_105717541.jpg"
				},
				"2_105717582": {
					"id": "2_105717582",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105717582.jpg"
				},
				"4_105697044": {
					"id": "4_105697044",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105697044.jpg"
				},
				"4_105717564": {
					"id": "4_105717564",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105717564.jpg"
				},
				"5_106778085": {
					"id": "5_106778085",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106778085.jpg"
				},
				"7_106778067": {
					"id": "7_106778067",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106778067.jpg"
				},
				"7_106778127": {
					"id": "7_106778127",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106778127.jpg"
				},
				"8_107597428": {
					"id": "8_107597428",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107597428.jpg"
				},
				"9_107597429": {
					"id": "9_107597429",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107597429.jpg"
				}
			},
			"name": "Zella Hybrid Tech Commuter Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "79.00",
					"maxItemPrice": "79.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-hybrid-tech-commuter-pants/5241711",
			"reviewCount": 24,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5260808": {
			"id": 5260808,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "5833195",
			"colorCount": 4,
			"colorDefaultId": "blossom pink",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107663980-5_107664405-15_107664235-19_107710979",
			"colorsById": {
				"blossom pink": {
					"id": "blossom pink",
					"label": "BLOSSOM PINK",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107663980",
						"1_107641321",
						"0_107641320"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "0_107663980"
				},
				"line grey": {
					"id": "line grey",
					"label": "LINE GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"5_107664405",
						"4_107641324",
						"2_107641322"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_107664405"
				},
				"safari taupe": {
					"id": "safari taupe",
					"label": "SAFARI TAUPE",
					"spriteIndex": 2,
					"mediaIds": [
						"15_107664235",
						"19_107641319",
						"18_107641318"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "15_107664235"
				},
				"sidewalk grey": {
					"id": "sidewalk grey",
					"label": "SIDEWALK GREY",
					"spriteIndex": 3,
					"mediaIds": [
						"19_107710979",
						"18_107692978",
						"1_107713981"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_107710979"
				}
			},
			"colorIds": [
				"blossom pink",
				"line grey",
				"safari taupe",
				"sidewalk grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107641320": {
					"id": "0_107641320",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107641320.jpg"
				},
				"0_107663980": {
					"id": "0_107663980",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107663980.jpg"
				},
				"15_107664235": {
					"id": "15_107664235",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107664235.jpg"
				},
				"18_107641318": {
					"id": "18_107641318",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107641318.jpg"
				},
				"18_107692978": {
					"id": "18_107692978",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107692978.jpg"
				},
				"19_107641319": {
					"id": "19_107641319",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107641319.jpg"
				},
				"19_107710979": {
					"id": "19_107710979",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107710979.jpg"
				},
				"1_107641321": {
					"id": "1_107641321",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107641321.jpg"
				},
				"1_107713981": {
					"id": "1_107713981",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107713981.jpg"
				},
				"2_107641322": {
					"id": "2_107641322",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107641322.jpg"
				},
				"4_107641324": {
					"id": "4_107641324",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107641324.jpg"
				},
				"5_107664405": {
					"id": "5_107664405",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107664405.jpg"
				}
			},
			"name": "ALLSAINTS Brace Slim Fit Solid Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "70.00",
					"maxItemPrice": "70.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-brace-slim-fit-solid-polo/5260808",
			"reviewCount": 6,
			"reviewStarRating": 3.8,
			"storeAvailability": null
		},
		"5261132": {
			"id": 5261132,
			"brandId": 1551,
			"brandName": "JOHN W. NORDSTROM",
			"styleNumber": "5833403",
			"colorCount": 3,
			"colorDefaultId": "grey phantom marl",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_106061929-19_106061939-18_106061918",
			"colorsById": {
				"black caviar": {
					"id": "black caviar",
					"label": "BLACK CAVIAR",
					"spriteIndex": 1,
					"mediaIds": [
						"19_106061939",
						"12_106064832",
						"11_106064851"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "19_106061939"
				},
				"grey phantom marl": {
					"id": "grey phantom marl",
					"label": "GREY PHANTOM MARL",
					"spriteIndex": 0,
					"mediaIds": [
						"9_106061929",
						"19_106064819",
						"6_106064826"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_106061929"
				},
				"tan dale": {
					"id": "tan dale",
					"label": "TAN DALE",
					"spriteIndex": 2,
					"mediaIds": [
						"18_106061918",
						"7_106064807",
						"13_106064813"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "18_106061918"
				}
			},
			"colorIds": [
				"grey phantom marl",
				"black caviar",
				"tan dale"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_106064851": {
					"id": "11_106064851",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106064851.jpg"
				},
				"12_106064832": {
					"id": "12_106064832",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106064832.jpg"
				},
				"13_106064813": {
					"id": "13_106064813",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106064813.jpg"
				},
				"18_106061918": {
					"id": "18_106061918",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106061918.jpg"
				},
				"19_106061939": {
					"id": "19_106061939",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106061939.jpg"
				},
				"19_106064819": {
					"id": "19_106064819",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106064819.jpg"
				},
				"6_106064826": {
					"id": "6_106064826",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106064826.jpg"
				},
				"7_106064807": {
					"id": "7_106064807",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106064807.jpg"
				},
				"9_106061929": {
					"id": "9_106061929",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106061929.jpg"
				}
			},
			"name": "John W. Nordstrom® Mason Wool & Cashmere Overcoat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "375.00",
					"maxItemPrice": "375.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/john-w-nordstrom-mason-wool-cashmere-overcoat/5261132",
			"reviewCount": 9,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5266082": {
			"id": 5266082,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5836925",
			"colorCount": 8,
			"colorDefaultId": "black linen texture",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_106175985-9_106542549-13_106557173-15_105307515-16_107545276-17_107028997-7_107538327-12_107538232",
			"colorsById": {
				"azure linen texture": {
					"id": "azure linen texture",
					"label": "AZURE LINEN TEXTURE",
					"spriteIndex": 1,
					"mediaIds": [
						"9_106542549",
						"11_106542591",
						"0_106542580"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_106542549"
				},
				"black camo": {
					"id": "black camo",
					"label": "BLACK CAMO",
					"spriteIndex": 2,
					"mediaIds": [
						"13_106557173",
						"16_106557116",
						"14_106557114"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_106557173"
				},
				"black linen texture": {
					"id": "black linen texture",
					"label": "BLACK LINEN TEXTURE",
					"spriteIndex": 0,
					"mediaIds": [
						"5_106175985",
						"16_106174836",
						"13_106174813"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "5_106175985"
				},
				"grey camo": {
					"id": "grey camo",
					"label": "GREY CAMO",
					"spriteIndex": 3,
					"mediaIds": [
						"15_105307515",
						"11_105307471",
						"4_105307544"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "15_105307515"
				},
				"grey linen texture": {
					"id": "grey linen texture",
					"label": "GREY LINEN TEXTURE",
					"spriteIndex": 4,
					"mediaIds": [
						"16_107545276",
						"17_107545277",
						"13_106174813"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "16_107545276"
				},
				"indigo multi palm": {
					"id": "indigo multi palm",
					"label": "INDIGO MULTI PALM",
					"spriteIndex": 5,
					"mediaIds": [
						"17_107028997",
						"3_107029163",
						"16_107029136"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "17_107028997"
				},
				"palm linen texture": {
					"id": "palm linen texture",
					"label": "PALM LINEN TEXTURE",
					"spriteIndex": 6,
					"mediaIds": [
						"7_107538327",
						"8_107538328",
						"2_107538322"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "7_107538327"
				},
				"sea glass linen texture stripe": {
					"id": "sea glass linen texture stripe",
					"label": "SEA GLASS LINEN TEXTURE STRIPE",
					"spriteIndex": 7,
					"mediaIds": [
						"12_107538232",
						"15_107538235",
						"18_107538218"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "12_107538232"
				}
			},
			"colorIds": [
				"black linen texture",
				"azure linen texture",
				"black camo",
				"grey camo",
				"grey linen texture",
				"indigo multi palm",
				"palm linen texture",
				"sea glass linen texture stripe"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106542580": {
					"id": "0_106542580",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106542580.jpg"
				},
				"11_105307471": {
					"id": "11_105307471",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105307471.jpg"
				},
				"11_106542591": {
					"id": "11_106542591",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106542591.jpg"
				},
				"12_107538232": {
					"id": "12_107538232",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107538232.jpg"
				},
				"13_106174813": {
					"id": "13_106174813",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106174813.jpg"
				},
				"13_106557173": {
					"id": "13_106557173",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106557173.jpg"
				},
				"14_106557114": {
					"id": "14_106557114",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106557114.jpg"
				},
				"15_105307515": {
					"id": "15_105307515",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105307515.jpg"
				},
				"15_107538235": {
					"id": "15_107538235",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107538235.jpg"
				},
				"16_106174836": {
					"id": "16_106174836",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106174836.jpg"
				},
				"16_106557116": {
					"id": "16_106557116",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106557116.jpg"
				},
				"16_107029136": {
					"id": "16_107029136",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107029136.jpg"
				},
				"16_107545276": {
					"id": "16_107545276",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107545276.jpg"
				},
				"17_107028997": {
					"id": "17_107028997",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107028997.jpg"
				},
				"17_107545277": {
					"id": "17_107545277",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107545277.jpg"
				},
				"18_107538218": {
					"id": "18_107538218",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107538218.jpg"
				},
				"2_107538322": {
					"id": "2_107538322",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107538322.jpg"
				},
				"3_107029163": {
					"id": "3_107029163",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107029163.jpg"
				},
				"4_105307544": {
					"id": "4_105307544",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105307544.jpg"
				},
				"5_106175985": {
					"id": "5_106175985",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106175985.jpg"
				},
				"7_107538327": {
					"id": "7_107538327",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107538327.jpg"
				},
				"8_107538328": {
					"id": "8_107538328",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107538328.jpg"
				},
				"9_106542549": {
					"id": "9_106542549",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106542549.jpg"
				}
			},
			"name": "vuori Banks Hybrid Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "68.00",
					"maxItemPrice": "68.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-banks-hybrid-shorts/5266082",
			"reviewCount": 22,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5272710": {
			"id": 5272710,
			"brandId": 12921,
			"brandName": "GOODLIFE",
			"styleNumber": "5841612",
			"colorCount": 4,
			"colorDefaultId": "moonlight jade",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_107604854-16_107758376-12_107604852-13_107604873",
			"colorsById": {
				"deep lichen green": {
					"id": "deep lichen green",
					"label": "DEEP LICHEN GREEN",
					"spriteIndex": 1,
					"mediaIds": [
						"16_107758376",
						"13_107747253",
						"12_107747252"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "16_107758376"
				},
				"limoges": {
					"id": "limoges",
					"label": "LIMOGES",
					"spriteIndex": 2,
					"mediaIds": [
						"12_107604852",
						"13_107627533",
						"5_107627525"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_107604852"
				},
				"moonlight jade": {
					"id": "moonlight jade",
					"label": "MOONLIGHT JADE",
					"spriteIndex": 0,
					"mediaIds": [
						"14_107604854",
						"12_107627672",
						"1_107627661"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "14_107604854"
				},
				"peach melba": {
					"id": "peach melba",
					"label": "PEACH MELBA",
					"spriteIndex": 3,
					"mediaIds": [
						"13_107604873",
						"18_107627458",
						"3_107627403"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "13_107604873"
				}
			},
			"colorIds": [
				"moonlight jade",
				"deep lichen green",
				"limoges",
				"peach melba"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107604852": {
					"id": "12_107604852",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107604852.jpg"
				},
				"12_107627672": {
					"id": "12_107627672",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107627672.jpg"
				},
				"12_107747252": {
					"id": "12_107747252",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107747252.jpg"
				},
				"13_107604873": {
					"id": "13_107604873",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107604873.jpg"
				},
				"13_107627533": {
					"id": "13_107627533",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107627533.jpg"
				},
				"13_107747253": {
					"id": "13_107747253",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107747253.jpg"
				},
				"14_107604854": {
					"id": "14_107604854",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107604854.jpg"
				},
				"16_107758376": {
					"id": "16_107758376",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107758376.jpg"
				},
				"18_107627458": {
					"id": "18_107627458",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107627458.jpg"
				},
				"1_107627661": {
					"id": "1_107627661",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107627661.jpg"
				},
				"3_107627403": {
					"id": "3_107627403",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107627403.jpg"
				},
				"5_107627525": {
					"id": "5_107627525",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107627525.jpg"
				}
			},
			"name": "Goodlife Sun Faded Cotton Slub T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "68.00",
					"maxItemPrice": "68.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/goodlife-sun-faded-cotton-slub-t-shirt/5272710",
			"reviewCount": 16,
			"reviewStarRating": 4.1,
			"storeAvailability": null
		},
		"5305983": {
			"id": 5305983,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "5862202",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_106745516",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"16_106745516",
						"18_106745518",
						"6_106393866"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "16_106745516"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_106745516": {
					"id": "16_106745516",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106745516.jpg"
				},
				"18_106745518": {
					"id": "18_106745518",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106745518.jpg"
				},
				"6_106393866": {
					"id": "6_106393866",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106393866.jpg"
				}
			},
			"name": "ALLSAINTS Milo Leather Biker Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "498.00",
					"maxItemPrice": "498.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-milo-leather-biker-jacket/5305983",
			"reviewCount": 8,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5320244": {
			"id": 5320244,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "5871203",
			"colorCount": 1,
			"colorDefaultId": "blue heaven chambray",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_106967671",
			"colorsById": {
				"blue heaven chambray": {
					"id": "blue heaven chambray",
					"label": "BLUE HEAVEN CHAMBRAY",
					"spriteIndex": 0,
					"mediaIds": [
						"11_106967671",
						"11_106967731",
						"14_106967714"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_106967671"
				}
			},
			"colorIds": [
				"blue heaven chambray"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_106967671": {
					"id": "11_106967671",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106967671.jpg"
				},
				"11_106967731": {
					"id": "11_106967731",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106967731.jpg"
				},
				"14_106967714": {
					"id": "14_106967714",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106967714.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Slim Fit Chambray Button-Down Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "69.50",
					"maxItemPrice": "69.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "27.80",
					"maxItemPrice": "27.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-slim-fit-chambray-button-down-shirt/5320244",
			"reviewCount": 10,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5333704": {
			"id": 5333704,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5879831",
			"colorCount": 1,
			"colorDefaultId": "blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_106964221",
			"colorsById": {
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"1_106964221",
						"15_106961275",
						"7_106961267"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_106964221"
				}
			},
			"colorIds": [
				"blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_106961275": {
					"id": "15_106961275",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106961275.jpg"
				},
				"1_106964221": {
					"id": "1_106964221",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106964221.jpg"
				},
				"7_106961267": {
					"id": "7_106961267",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106961267.jpg"
				}
			},
			"name": "Ted Baker London Jay Trim Fit Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "798.00",
					"maxItemPrice": "798.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-jay-trim-fit-wool-suit/5333704",
			"reviewCount": 3,
			"reviewStarRating": 3.7,
			"storeAvailability": null
		},
		"5340999": {
			"id": 5340999,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5883295",
			"colorCount": 7,
			"colorDefaultId": "khaki",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107606240-14_106747434-0_107710880-8_107606248-19_107606239-14_107677094-2_106747442",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_106747434",
						"18_106751978",
						"16_106751976"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_106747434"
				},
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 2,
					"mediaIds": [
						"0_107710880",
						"6_107717446",
						"5_107717445"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_107710880"
				},
				"deep pink": {
					"id": "deep pink",
					"label": "DEEP PINK",
					"spriteIndex": 3,
					"mediaIds": [
						"8_107606248",
						"16_107625456",
						"15_107625455"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "8_107606248"
				},
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 4,
					"mediaIds": [
						"19_107606239",
						"1_107625521",
						"0_107625520"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_107606239"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107606240",
						"16_107625516",
						"15_107625515"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "0_107606240"
				},
				"lilac": {
					"id": "lilac",
					"label": "LILAC",
					"spriteIndex": 5,
					"mediaIds": [
						"14_107677094",
						"7_107678287",
						"1_107678281"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "14_107677094"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 6,
					"mediaIds": [
						"2_106747442",
						"3_106752083",
						"19_106752079"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_106747442"
				}
			},
			"colorIds": [
				"khaki",
				"black",
				"blue",
				"deep pink",
				"grey",
				"lilac",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107606240": {
					"id": "0_107606240",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107606240.jpg"
				},
				"0_107625520": {
					"id": "0_107625520",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107625520.jpg"
				},
				"0_107710880": {
					"id": "0_107710880",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107710880.jpg"
				},
				"14_106747434": {
					"id": "14_106747434",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106747434.jpg"
				},
				"14_107677094": {
					"id": "14_107677094",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107677094.jpg"
				},
				"15_107625455": {
					"id": "15_107625455",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107625455.jpg"
				},
				"15_107625515": {
					"id": "15_107625515",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107625515.jpg"
				},
				"16_106751976": {
					"id": "16_106751976",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106751976.jpg"
				},
				"16_107625456": {
					"id": "16_107625456",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107625456.jpg"
				},
				"16_107625516": {
					"id": "16_107625516",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107625516.jpg"
				},
				"18_106751978": {
					"id": "18_106751978",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106751978.jpg"
				},
				"19_106752079": {
					"id": "19_106752079",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106752079.jpg"
				},
				"19_107606239": {
					"id": "19_107606239",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107606239.jpg"
				},
				"1_107625521": {
					"id": "1_107625521",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107625521.jpg"
				},
				"1_107678281": {
					"id": "1_107678281",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107678281.jpg"
				},
				"2_106747442": {
					"id": "2_106747442",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106747442.jpg"
				},
				"3_106752083": {
					"id": "3_106752083",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106752083.jpg"
				},
				"5_107717445": {
					"id": "5_107717445",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107717445.jpg"
				},
				"6_107717446": {
					"id": "6_107717446",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107717446.jpg"
				},
				"7_107678287": {
					"id": "7_107678287",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107678287.jpg"
				},
				"8_107606248": {
					"id": "8_107606248",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107606248.jpg"
				}
			},
			"name": "Ted Baker London Tortila Slim Fit Tipped Pocket Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "99.00",
					"maxItemPrice": "99.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-tortila-slim-fit-tipped-pocket-polo/5340999",
			"reviewCount": 23,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5344935": {
			"id": 5344935,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "5884919",
			"colorCount": 2,
			"colorDefaultId": "navy blazer",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_106549873-14_106549974",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_106549974",
						"7_106550247",
						"2_106550082"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_106549974"
				},
				"navy blazer": {
					"id": "navy blazer",
					"label": "NAVY BLAZER",
					"spriteIndex": 0,
					"mediaIds": [
						"13_106549873",
						"14_106549954",
						"0_106549940"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_106549873"
				}
			},
			"colorIds": [
				"navy blazer",
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106549940": {
					"id": "0_106549940",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106549940.jpg"
				},
				"13_106549873": {
					"id": "13_106549873",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106549873.jpg"
				},
				"14_106549954": {
					"id": "14_106549954",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106549954.jpg"
				},
				"14_106549974": {
					"id": "14_106549974",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106549974.jpg"
				},
				"2_106550082": {
					"id": "2_106550082",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106550082.jpg"
				},
				"7_106550247": {
					"id": "7_106550247",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106550247.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Performance Flat Front Stretch Chino Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "79.50",
					"maxItemPrice": "79.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "39.75",
					"maxItemPrice": "39.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-performance-flat-front-stretch-chino-pants/5344935",
			"reviewCount": 5,
			"reviewStarRating": 3.8,
			"storeAvailability": null
		},
		"5345644": {
			"id": 5345644,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5885380",
			"colorCount": 1,
			"colorDefaultId": "navy india ink",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_106903948",
			"colorsById": {
				"navy india ink": {
					"id": "navy india ink",
					"label": "NAVY INDIA INK",
					"spriteIndex": 0,
					"mediaIds": [
						"8_106903948",
						"15_106903955",
						"14_106903954"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_106903948"
				}
			},
			"colorIds": [
				"navy india ink"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_106903954": {
					"id": "14_106903954",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106903954.jpg"
				},
				"15_106903955": {
					"id": "15_106903955",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106903955.jpg"
				},
				"8_106903948": {
					"id": "8_106903948",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106903948.jpg"
				}
			},
			"name": "1901 Ballard Slim Fit Peached Twill Chino Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "29.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-ballard-slim-fit-peached-twill-chino-pants/5345644",
			"reviewCount": 31,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5349956": {
			"id": 5349956,
			"brandId": 16393,
			"brandName": "CHAMPION",
			"styleNumber": "5888145",
			"colorCount": 4,
			"colorDefaultId": "c gold",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_107081555-1_107081561-12_107081532-6_107081526",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"1_107081561",
						"2_107081542",
						"11_106869931"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "1_107081561"
				},
				"c gold": {
					"id": "c gold",
					"label": "C GOLD",
					"spriteIndex": 0,
					"mediaIds": [
						"15_107081555",
						"18_107081558",
						"11_106869931"
					],
					"standardColors": [
						"Yellow"
					],
					"swatchMediaId": "15_107081555"
				},
				"oxford grey": {
					"id": "oxford grey",
					"label": "OXFORD GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"12_107081532",
						"13_107081533",
						"11_106869931"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "12_107081532"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 3,
					"mediaIds": [
						"6_107081526",
						"9_107081529",
						"11_106869931"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "6_107081526"
				}
			},
			"colorIds": [
				"c gold",
				"black",
				"oxford grey",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_106869931": {
					"id": "11_106869931",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106869931.jpg"
				},
				"12_107081532": {
					"id": "12_107081532",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107081532.jpg"
				},
				"13_107081533": {
					"id": "13_107081533",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107081533.jpg"
				},
				"15_107081555": {
					"id": "15_107081555",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107081555.jpg"
				},
				"18_107081558": {
					"id": "18_107081558",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107081558.jpg"
				},
				"1_107081561": {
					"id": "1_107081561",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107081561.jpg"
				},
				"2_107081542": {
					"id": "2_107081542",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107081542.jpg"
				},
				"6_107081526": {
					"id": "6_107081526",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107081526.jpg"
				},
				"9_107081529": {
					"id": "9_107081529",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107081529.jpg"
				}
			},
			"name": "Champion Heritage Script Logo T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "25.00",
					"maxItemPrice": "25.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/champion-heritage-script-logo-t-shirt/5349956",
			"reviewCount": 61,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5350172": {
			"id": 5350172,
			"brandId": 11669,
			"brandName": "MADEWELL",
			"styleNumber": "5888498",
			"colorCount": 7,
			"colorDefaultId": "cool dawn",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_107829491-18_107103078-12_107103512-9_107549329-2_106904562-16_107056596-17_107102597",
			"colorsById": {
				"baltic blue": {
					"id": "baltic blue",
					"label": "BALTIC BLUE",
					"spriteIndex": 1,
					"mediaIds": [
						"18_107103078",
						"6_107103166",
						"18_107103158"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_107103078"
				},
				"british surplus": {
					"id": "british surplus",
					"label": "BRITISH SURPLUS",
					"spriteIndex": 2,
					"mediaIds": [
						"12_107103512",
						"1_107103521",
						"18_107103518"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "12_107103512"
				},
				"cool dawn": {
					"id": "cool dawn",
					"label": "COOL DAWN",
					"spriteIndex": 0,
					"mediaIds": [
						"11_107829491",
						"18_107829558",
						"5_107549305"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_107829491"
				},
				"faded peach": {
					"id": "faded peach",
					"label": "FADED PEACH",
					"spriteIndex": 3,
					"mediaIds": [
						"9_107549329",
						"11_107549331",
						"5_107549305"
					],
					"standardColors": [
						"Orange",
						"Pink"
					],
					"swatchMediaId": "9_107549329"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 4,
					"mediaIds": [
						"2_106904562",
						"6_106904566",
						"19_106904539"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_106904562"
				},
				"lighthouse": {
					"id": "lighthouse",
					"label": "LIGHTHOUSE",
					"spriteIndex": 5,
					"mediaIds": [
						"16_107056596",
						"4_107056644",
						"9_107056629"
					],
					"standardColors": [
						"Offwhite"
					],
					"swatchMediaId": "16_107056596"
				},
				"weathered brick": {
					"id": "weathered brick",
					"label": "WEATHERED BRICK",
					"spriteIndex": 6,
					"mediaIds": [
						"17_107102597",
						"7_107102647",
						"10_107102630"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "17_107102597"
				}
			},
			"colorIds": [
				"cool dawn",
				"baltic blue",
				"british surplus",
				"faded peach",
				"heather grey",
				"lighthouse",
				"weathered brick"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107102630": {
					"id": "10_107102630",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107102630.jpg"
				},
				"11_107549331": {
					"id": "11_107549331",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107549331.jpg"
				},
				"11_107829491": {
					"id": "11_107829491",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107829491.jpg"
				},
				"12_107103512": {
					"id": "12_107103512",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107103512.jpg"
				},
				"16_107056596": {
					"id": "16_107056596",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107056596.jpg"
				},
				"17_107102597": {
					"id": "17_107102597",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107102597.jpg"
				},
				"18_107103078": {
					"id": "18_107103078",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107103078.jpg"
				},
				"18_107103158": {
					"id": "18_107103158",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107103158.jpg"
				},
				"18_107103518": {
					"id": "18_107103518",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107103518.jpg"
				},
				"18_107829558": {
					"id": "18_107829558",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107829558.jpg"
				},
				"19_106904539": {
					"id": "19_106904539",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106904539.jpg"
				},
				"1_107103521": {
					"id": "1_107103521",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107103521.jpg"
				},
				"2_106904562": {
					"id": "2_106904562",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106904562.jpg"
				},
				"4_107056644": {
					"id": "4_107056644",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107056644.jpg"
				},
				"5_107549305": {
					"id": "5_107549305",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107549305.jpg"
				},
				"6_106904566": {
					"id": "6_106904566",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106904566.jpg"
				},
				"6_107103166": {
					"id": "6_107103166",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107103166.jpg"
				},
				"7_107102647": {
					"id": "7_107102647",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107102647.jpg"
				},
				"9_107056629": {
					"id": "9_107056629",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107056629.jpg"
				},
				"9_107549329": {
					"id": "9_107549329",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107549329.jpg"
				}
			},
			"name": "Madewell Garment Dyed Allday Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "29.50",
					"maxItemPrice": "29.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/madewell-garment-dyed-allday-crewneck-t-shirt/5350172",
			"reviewCount": 11,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5358675": {
			"id": 5358675,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5894629",
			"colorCount": 3,
			"colorDefaultId": "northern night",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_106389524-10_106203290-14_106389514",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"10_106203290",
						"7_106203307",
						"1_106203301"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_106203290"
				},
				"iron grey": {
					"id": "iron grey",
					"label": "IRON GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"14_106389514",
						"11_106389531",
						"0_106389520"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "14_106389514"
				},
				"northern night": {
					"id": "northern night",
					"label": "NORTHERN NIGHT",
					"spriteIndex": 0,
					"mediaIds": [
						"4_106389524",
						"17_106389537",
						"16_106389536"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_106389524"
				}
			},
			"colorIds": [
				"northern night",
				"black",
				"iron grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106389520": {
					"id": "0_106389520",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106389520.jpg"
				},
				"10_106203290": {
					"id": "10_106203290",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106203290.jpg"
				},
				"11_106389531": {
					"id": "11_106389531",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106389531.jpg"
				},
				"14_106389514": {
					"id": "14_106389514",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106389514.jpg"
				},
				"16_106389536": {
					"id": "16_106389536",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106389536.jpg"
				},
				"17_106389537": {
					"id": "17_106389537",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106389537.jpg"
				},
				"1_106203301": {
					"id": "1_106203301",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106203301.jpg"
				},
				"4_106389524": {
					"id": "4_106389524",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106389524.jpg"
				},
				"7_106203307": {
					"id": "7_106203307",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106203307.jpg"
				}
			},
			"name": "Canada Goose Windbridge Zip Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "525.00",
					"maxItemPrice": "525.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-windbridge-zip-hoodie/5358675",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5365627": {
			"id": 5365627,
			"brandId": 260,
			"brandName": "FRENCH CONNECTION",
			"styleNumber": "5898428",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_106492037",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"17_106492037",
						"10_106486270",
						"9_106486249"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "17_106492037"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106486270": {
					"id": "10_106486270",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106486270.jpg"
				},
				"17_106492037": {
					"id": "17_106492037",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106492037.jpg"
				},
				"9_106486249": {
					"id": "9_106486249",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106486249.jpg"
				}
			},
			"name": "French Connection Milano Regular Fit Crewneck Sweater",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "88.00",
					"maxItemPrice": "88.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "44.00",
					"maxItemPrice": "44.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/french-connection-milano-regular-fit-crewneck-sweater/5365627",
			"reviewCount": 4,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5392425": {
			"id": 5392425,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "1083720_3",
			"colorCount": 4,
			"colorDefaultId": "white brilliant",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_105854025-18_105863218-6_106107046-5_105852845",
			"colorsById": {
				"blue azurite": {
					"id": "blue azurite",
					"label": "BLUE AZURITE",
					"spriteIndex": 1,
					"mediaIds": [
						"18_105863218",
						"19_105863219"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_105863218"
				},
				"blue surf": {
					"id": "blue surf",
					"label": "BLUE SURF",
					"spriteIndex": 2,
					"mediaIds": [
						"6_106107046",
						"7_103703067"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_106107046"
				},
				"grey castlerock": {
					"id": "grey castlerock",
					"label": "GREY CASTLEROCK",
					"spriteIndex": 3,
					"mediaIds": [
						"5_105852845",
						"15_105852835"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "5_105852845"
				},
				"white brilliant": {
					"id": "white brilliant",
					"label": "WHITE BRILLIANT",
					"spriteIndex": 0,
					"mediaIds": [
						"5_105854025",
						"10_105854010"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "5_105854025"
				}
			},
			"colorIds": [
				"white brilliant",
				"blue azurite",
				"blue surf",
				"grey castlerock"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_105854010": {
					"id": "10_105854010",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_105854010.jpg"
				},
				"15_105852835": {
					"id": "15_105852835",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105852835.jpg"
				},
				"18_105863218": {
					"id": "18_105863218",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_105863218.jpg"
				},
				"19_105863219": {
					"id": "19_105863219",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_105863219.jpg"
				},
				"5_105852845": {
					"id": "5_105852845",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105852845.jpg"
				},
				"5_105854025": {
					"id": "5_105854025",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_105854025.jpg"
				},
				"6_106107046": {
					"id": "6_106107046",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106107046.jpg"
				},
				"7_103703067": {
					"id": "7_103703067",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_103703067.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Classic Fit Non-Iron Solid Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-classic-fit-non-iron-solid-dress-shirt/5392425",
			"reviewCount": 145,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5400840": {
			"id": 5400840,
			"brandId": 6267,
			"brandName": "RAG AND BONE",
			"styleNumber": "5922939",
			"colorCount": 5,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_107255548-15_107256255-4_107002244-12_107256272-7_107001927",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"15_107256255",
						"10_107256270",
						"7_107256267"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "15_107256255"
				},
				"grey heather": {
					"id": "grey heather",
					"label": "GREY HEATHER",
					"spriteIndex": 2,
					"mediaIds": [
						"4_107002244",
						"16_107002296",
						"9_107002269"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "4_107002244"
				},
				"lakeblu": {
					"id": "lakeblu",
					"label": "LAKEBLU",
					"spriteIndex": 3,
					"mediaIds": [
						"12_107256272",
						"14_107255534",
						"3_107255523"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_107256272"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"8_107255548",
						"18_107255758",
						"6_107255726"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_107255548"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 4,
					"mediaIds": [
						"7_107001927",
						"4_107001944",
						"0_107001940"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "7_107001927"
				}
			},
			"colorIds": [
				"navy",
				"black",
				"grey heather",
				"lakeblu",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107001940": {
					"id": "0_107001940",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107001940.jpg"
				},
				"10_107256270": {
					"id": "10_107256270",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107256270.jpg"
				},
				"12_107256272": {
					"id": "12_107256272",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107256272.jpg"
				},
				"14_107255534": {
					"id": "14_107255534",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107255534.jpg"
				},
				"15_107256255": {
					"id": "15_107256255",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107256255.jpg"
				},
				"16_107002296": {
					"id": "16_107002296",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107002296.jpg"
				},
				"18_107255758": {
					"id": "18_107255758",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107255758.jpg"
				},
				"3_107255523": {
					"id": "3_107255523",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107255523.jpg"
				},
				"4_107001944": {
					"id": "4_107001944",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107001944.jpg"
				},
				"4_107002244": {
					"id": "4_107002244",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107002244.jpg"
				},
				"6_107255726": {
					"id": "6_107255726",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107255726.jpg"
				},
				"7_107001927": {
					"id": "7_107001927",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107001927.jpg"
				},
				"7_107256267": {
					"id": "7_107256267",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107256267.jpg"
				},
				"8_107255548": {
					"id": "8_107255548",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107255548.jpg"
				},
				"9_107002269": {
					"id": "9_107002269",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107002269.jpg"
				}
			},
			"name": "rag & bone Interlock Slim Fit Heathered Polo Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "125.00",
					"maxItemPrice": "125.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/rag-bone-interlock-slim-fit-heathered-polo-shirt/5400840",
			"reviewCount": 7,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5401057": {
			"id": 5401057,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5923181",
			"colorCount": 6,
			"colorDefaultId": "heather grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_106163780-2_107841502-6_106163826-18_107840318-16_107433276-19_107021739",
			"colorsById": {
				"army heather": {
					"id": "army heather",
					"label": "ARMY HEATHER",
					"spriteIndex": 1,
					"mediaIds": [
						"2_107841502",
						"19_107808839",
						"5_106163785"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "2_107841502"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"6_106163826",
						"2_106163922",
						"16_106163916"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "6_106163826"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"0_106163780",
						"4_106163804",
						"5_106163785"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "0_106163780"
				},
				"palm heather": {
					"id": "palm heather",
					"label": "PALM HEATHER",
					"spriteIndex": 3,
					"mediaIds": [
						"18_107840318",
						"3_107823723",
						"5_106163785"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "18_107840318"
				},
				"sapphire heather": {
					"id": "sapphire heather",
					"label": "SAPPHIRE HEATHER",
					"spriteIndex": 4,
					"mediaIds": [
						"16_107433276",
						"5_107442965",
						"17_107433317"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_107433276"
				},
				"sea glass heather": {
					"id": "sea glass heather",
					"label": "SEA GLASS HEATHER",
					"spriteIndex": 5,
					"mediaIds": [
						"19_107021739",
						"4_107021824",
						"4_107021784"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "19_107021739"
				}
			},
			"colorIds": [
				"heather grey",
				"army heather",
				"black",
				"palm heather",
				"sapphire heather",
				"sea glass heather"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106163780": {
					"id": "0_106163780",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106163780.jpg"
				},
				"16_106163916": {
					"id": "16_106163916",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106163916.jpg"
				},
				"16_107433276": {
					"id": "16_107433276",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107433276.jpg"
				},
				"17_107433317": {
					"id": "17_107433317",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107433317.jpg"
				},
				"18_107840318": {
					"id": "18_107840318",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107840318.jpg"
				},
				"19_107021739": {
					"id": "19_107021739",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107021739.jpg"
				},
				"19_107808839": {
					"id": "19_107808839",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107808839.jpg"
				},
				"2_106163922": {
					"id": "2_106163922",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106163922.jpg"
				},
				"2_107841502": {
					"id": "2_107841502",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107841502.jpg"
				},
				"3_107823723": {
					"id": "3_107823723",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107823723.jpg"
				},
				"4_106163804": {
					"id": "4_106163804",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106163804.jpg"
				},
				"4_107021784": {
					"id": "4_107021784",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107021784.jpg"
				},
				"4_107021824": {
					"id": "4_107021824",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107021824.jpg"
				},
				"5_106163785": {
					"id": "5_106163785",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106163785.jpg"
				},
				"5_107442965": {
					"id": "5_107442965",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107442965.jpg"
				},
				"6_106163826": {
					"id": "6_106163826",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106163826.jpg"
				}
			},
			"name": "vuori Tradewind Pocket Performance T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "48.00",
					"maxItemPrice": "48.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-tradewind-pocket-performance-t-shirt/5401057",
			"reviewCount": 6,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5401058": {
			"id": 5401058,
			"brandId": 12572,
			"brandName": "VUORI",
			"styleNumber": "5923178",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_106392580-13_106178513",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"0_106392580",
						"12_106412252",
						"4_106392584"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_106392580"
				},
				"charcoal heather": {
					"id": "charcoal heather",
					"label": "CHARCOAL HEATHER",
					"spriteIndex": 1,
					"mediaIds": [
						"13_106178513",
						"6_106174786",
						"10_106174770"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "13_106178513"
				}
			},
			"colorIds": [
				"black",
				"charcoal heather"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106392580": {
					"id": "0_106392580",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106392580.jpg"
				},
				"10_106174770": {
					"id": "10_106174770",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106174770.jpg"
				},
				"12_106412252": {
					"id": "12_106412252",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106412252.jpg"
				},
				"13_106178513": {
					"id": "13_106178513",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106178513.jpg"
				},
				"4_106392584": {
					"id": "4_106392584",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106392584.jpg"
				},
				"6_106174786": {
					"id": "6_106174786",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106174786.jpg"
				}
			},
			"name": "vuori Sunday Performance Jogger Sweatpants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "89.00",
					"maxItemPrice": "89.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vuori-sunday-performance-jogger-sweatpants/5401058",
			"reviewCount": 6,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5414900": {
			"id": 5414900,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5933059",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_106929961",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"1_106929961",
						"4_106929984",
						"17_106929977"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "1_106929961"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"17_106929977": {
					"id": "17_106929977",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106929977.jpg"
				},
				"1_106929961": {
					"id": "1_106929961",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106929961.jpg"
				},
				"4_106929984": {
					"id": "4_106929984",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106929984.jpg"
				}
			},
			"name": "Zella Core Stretch Woven Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.00",
					"maxItemPrice": "59.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-core-stretch-woven-pants/5414900",
			"reviewCount": 14,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5415785": {
			"id": 5415785,
			"brandId": 304,
			"brandName": "HART SCHAFFNER MARX",
			"styleNumber": "5933483",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107393660",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107393660",
						"3_107394503",
						"2_107394502"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_107393660"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107393660": {
					"id": "0_107393660",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107393660.jpg"
				},
				"2_107394502": {
					"id": "2_107394502",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107394502.jpg"
				},
				"3_107394503": {
					"id": "3_107394503",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107394503.jpg"
				}
			},
			"name": "Hart Schaffner Marx New York Classic Fit Solid Stretch Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "795.00",
					"maxItemPrice": "795.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/hart-schaffner-marx-new-york-classic-fit-solid-stretch-wool-suit/5415785",
			"reviewCount": 1,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5420959": {
			"id": 5420959,
			"brandId": 7260,
			"brandName": "TRAVISMATHEW",
			"styleNumber": "5937714",
			"colorCount": 6,
			"colorDefaultId": "heather dark red",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107397376-7_107389847-7_107504127-5_107389985-8_107504148-1_107389901",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"7_107389847",
						"14_107389914",
						"4_107389864"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "7_107389847"
				},
				"heather allure": {
					"id": "heather allure",
					"label": "HEATHER ALLURE",
					"spriteIndex": 2,
					"mediaIds": [
						"7_107504127",
						"5_107504125",
						"7_107504147"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_107504127"
				},
				"heather blue nights": {
					"id": "heather blue nights",
					"label": "HEATHER BLUE NIGHTS",
					"spriteIndex": 3,
					"mediaIds": [
						"5_107389985",
						"11_107390031",
						"18_107390018"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107389985"
				},
				"heather dark red": {
					"id": "heather dark red",
					"label": "HEATHER DARK RED",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107397376",
						"13_107399213",
						"7_107397387"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "16_107397376"
				},
				"heather grey pinstripe": {
					"id": "heather grey pinstripe",
					"label": "HEATHER GREY PINSTRIPE",
					"spriteIndex": 4,
					"mediaIds": [
						"8_107504148",
						"6_107504146",
						"19_107504139"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "8_107504148"
				},
				"heather provincial blue": {
					"id": "heather provincial blue",
					"label": "HEATHER PROVINCIAL BLUE",
					"spriteIndex": 5,
					"mediaIds": [
						"1_107389901",
						"12_107389992",
						"2_107389962"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_107389901"
				}
			},
			"colorIds": [
				"heather dark red",
				"black",
				"heather allure",
				"heather blue nights",
				"heather grey pinstripe",
				"heather provincial blue"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107390031": {
					"id": "11_107390031",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107390031.jpg"
				},
				"12_107389992": {
					"id": "12_107389992",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107389992.jpg"
				},
				"13_107399213": {
					"id": "13_107399213",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107399213.jpg"
				},
				"14_107389914": {
					"id": "14_107389914",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107389914.jpg"
				},
				"16_107397376": {
					"id": "16_107397376",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107397376.jpg"
				},
				"18_107390018": {
					"id": "18_107390018",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107390018.jpg"
				},
				"19_107504139": {
					"id": "19_107504139",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107504139.jpg"
				},
				"1_107389901": {
					"id": "1_107389901",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107389901.jpg"
				},
				"2_107389962": {
					"id": "2_107389962",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107389962.jpg"
				},
				"4_107389864": {
					"id": "4_107389864",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107389864.jpg"
				},
				"5_107389985": {
					"id": "5_107389985",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107389985.jpg"
				},
				"5_107504125": {
					"id": "5_107504125",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107504125.jpg"
				},
				"6_107504146": {
					"id": "6_107504146",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107504146.jpg"
				},
				"7_107389847": {
					"id": "7_107389847",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107389847.jpg"
				},
				"7_107397387": {
					"id": "7_107397387",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107397387.jpg"
				},
				"7_107504127": {
					"id": "7_107504127",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107504127.jpg"
				},
				"7_107504147": {
					"id": "7_107504147",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107504147.jpg"
				},
				"8_107504148": {
					"id": "8_107504148",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107504148.jpg"
				}
			},
			"name": "TravisMathew Trumbull V-Neck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.95",
					"maxItemPrice": "59.95",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 33,
					"maxItemPercentOff": 33,
					"minItemPrice": "40.17",
					"maxItemPrice": "40.17",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/travismathew-trumbull-v-neck-t-shirt/5420959",
			"reviewCount": 3,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5423437": {
			"id": 5423437,
			"brandId": 18457,
			"brandName": "BOMBAS",
			"styleNumber": "5939044",
			"colorCount": 2,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_106584989-18_106584998",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"18_106584998",
						"2_106585002",
						"1_106585001"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_106584998"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"9_106584989",
						"15_106584995",
						"12_106584992"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "9_106584989"
				}
			},
			"colorIds": [
				"white",
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_106584992": {
					"id": "12_106584992",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106584992.jpg"
				},
				"15_106584995": {
					"id": "15_106584995",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106584995.jpg"
				},
				"18_106584998": {
					"id": "18_106584998",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_106584998.jpg"
				},
				"1_106585001": {
					"id": "1_106585001",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106585001.jpg"
				},
				"2_106585002": {
					"id": "2_106585002",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106585002.jpg"
				},
				"9_106584989": {
					"id": "9_106584989",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106584989.jpg"
				}
			},
			"name": "Bombas Solids Ankle Socks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "12.00",
					"maxItemPrice": "12.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bombas-solids-ankle-socks/5423437",
			"reviewCount": 9,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5425442": {
			"id": 5425442,
			"brandId": 4388,
			"brandName": "CANALI",
			"styleNumber": "5940540",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107245076",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107245076",
						"8_107245308",
						"4_107245204"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_107245076"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_107245076": {
					"id": "16_107245076",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107245076.jpg"
				},
				"4_107245204": {
					"id": "4_107245204",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107245204.jpg"
				},
				"8_107245308": {
					"id": "8_107245308",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107245308.jpg"
				}
			},
			"name": "Canali Siena Soft Classic Fit Check Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "2,195.00",
					"maxItemPrice": "2,195.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 55,
					"maxItemPercentOff": 55,
					"minItemPrice": "987.75",
					"maxItemPrice": "987.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canali-siena-soft-classic-fit-check-wool-suit/5425442",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5428260": {
			"id": 5428260,
			"brandId": 3839,
			"brandName": "VINCE CAMUTO",
			"styleNumber": "5941624",
			"colorCount": 1,
			"colorDefaultId": "space dye grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107018718",
			"colorsById": {
				"space dye grey": {
					"id": "space dye grey",
					"label": "SPACE DYE GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107018718",
						"13_107016153",
						"3_107015803"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_107018718"
				}
			},
			"colorIds": [
				"space dye grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_107016153": {
					"id": "13_107016153",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107016153.jpg"
				},
				"18_107018718": {
					"id": "18_107018718",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107018718.jpg"
				},
				"3_107015803": {
					"id": "3_107015803",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107015803.jpg"
				}
			},
			"name": "Vince Camuto Stretch Performance Sport Coat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "225.00",
					"maxItemPrice": "225.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "90.00",
					"maxItemPrice": "90.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vince-camuto-stretch-performance-sport-coat/5428260",
			"reviewCount": 3,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5429954": {
			"id": 5429954,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "5942307",
			"colorCount": 1,
			"colorDefaultId": "grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107500781",
			"colorsById": {
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107500781",
						"4_107500784",
						"8_107500628"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "1_107500781"
				}
			},
			"colorIds": [
				"grey"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"1_107500781": {
					"id": "1_107500781",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107500781.jpg"
				},
				"4_107500784": {
					"id": "4_107500784",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107500784.jpg"
				},
				"8_107500628": {
					"id": "8_107500628",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107500628.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Zip Cotton Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "348.00",
					"maxItemPrice": "348.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-zip-cotton-hoodie/5429954",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5430012": {
			"id": 5430012,
			"brandId": 5446,
			"brandName": "VERSACE",
			"styleNumber": "5942327",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=3_106323343",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"3_106323343",
						"17_106323337",
						"0_106316680"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "3_106323343"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106316680": {
					"id": "0_106316680",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106316680.jpg"
				},
				"17_106323337": {
					"id": "17_106323337",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106323337.jpg"
				},
				"3_106323343": {
					"id": "3_106323343",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106323343.jpg"
				}
			},
			"name": "Versace Barocco Terry Robe",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "595.00",
					"maxItemPrice": "595.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/versace-barocco-terry-robe/5430012",
			"reviewCount": 3,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5431627": {
			"id": 5431627,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "1083669_3",
			"colorCount": 4,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_104853136-19_103226739-10_107435990-16_105732256",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"16_104853136",
						"10_104853130",
						"0_105869800"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "16_104853136"
				},
				"lavender spray": {
					"id": "lavender spray",
					"label": "LAVENDER SPRAY",
					"spriteIndex": 1,
					"mediaIds": [
						"19_103226739",
						"0_103226740",
						"12_103226092"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "19_103226739"
				},
				"navy medieval": {
					"id": "navy medieval",
					"label": "NAVY MEDIEVAL",
					"spriteIndex": 2,
					"mediaIds": [
						"10_107435990",
						"19_107436119",
						"0_105869800"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_107435990"
				},
				"pink nostalgia": {
					"id": "pink nostalgia",
					"label": "PINK NOSTALGIA",
					"spriteIndex": 3,
					"mediaIds": [
						"16_105732256",
						"15_105732255",
						"13_105732253"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "16_105732256"
				}
			},
			"colorIds": [
				"black",
				"lavender spray",
				"navy medieval",
				"pink nostalgia"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_103226740": {
					"id": "0_103226740",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_103226740.jpg"
				},
				"0_105869800": {
					"id": "0_105869800",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105869800.jpg"
				},
				"10_104853130": {
					"id": "10_104853130",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_104853130.jpg"
				},
				"10_107435990": {
					"id": "10_107435990",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107435990.jpg"
				},
				"12_103226092": {
					"id": "12_103226092",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_103226092.jpg"
				},
				"13_105732253": {
					"id": "13_105732253",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_105732253.jpg"
				},
				"15_105732255": {
					"id": "15_105732255",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105732255.jpg"
				},
				"16_104853136": {
					"id": "16_104853136",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_104853136.jpg"
				},
				"16_105732256": {
					"id": "16_105732256",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_105732256.jpg"
				},
				"19_103226739": {
					"id": "19_103226739",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_103226739.jpg"
				},
				"19_107436119": {
					"id": "19_107436119",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107436119.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Traditional Fit Non-Iron Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.50",
					"maxItemPrice": "49.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 20,
					"maxItemPercentOff": 50,
					"minItemPrice": "19.80",
					"maxItemPrice": "39.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-traditional-fit-non-iron-dress-shirt/5431627",
			"reviewCount": 152,
			"reviewStarRating": 4.2,
			"storeAvailability": null
		},
		"5435855": {
			"id": 5435855,
			"brandId": 998,
			"brandName": "FENDI",
			"styleNumber": "5944899",
			"colorCount": 1,
			"colorDefaultId": "tobacco/ black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107536632",
			"colorsById": {
				"tobacco/ black": {
					"id": "tobacco/ black",
					"label": "TOBACCO/ BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107536632",
						"7_107536627",
						"6_107536626"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "12_107536632"
				}
			},
			"colorIds": [
				"tobacco/ black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107536632": {
					"id": "12_107536632",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107536632.jpg"
				},
				"6_107536626": {
					"id": "6_107536626",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107536626.jpg"
				},
				"7_107536627": {
					"id": "7_107536627",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107536627.jpg"
				}
			},
			"name": "Fendi FF Logo Print Cotton T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "630.00",
					"maxItemPrice": "630.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/fendi-ff-logo-print-cotton-t-shirt/5435855",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5437029": {
			"id": 5437029,
			"brandId": 1354,
			"brandName": "DAVID DONAHUE",
			"styleNumber": "5945660",
			"colorCount": 1,
			"colorDefaultId": "white/ blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_106993509",
			"colorsById": {
				"white/ blue": {
					"id": "white/ blue",
					"label": "WHITE/ BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"9_106993509",
						"9_107007769",
						"15_106993475"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_106993509"
				}
			},
			"colorIds": [
				"white/ blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_106993475": {
					"id": "15_106993475",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106993475.jpg"
				},
				"9_106993509": {
					"id": "9_106993509",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106993509.jpg"
				},
				"9_107007769": {
					"id": "9_107007769",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107007769.jpg"
				}
			},
			"name": "David Donahue Trim Fit Check Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "145.00",
					"maxItemPrice": "145.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 62,
					"maxItemPercentOff": 62,
					"minItemPrice": "54.98",
					"maxItemPrice": "54.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/david-donahue-trim-fit-check-dress-shirt/5437029",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5447107": {
			"id": 5447107,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5953448",
			"colorCount": 1,
			"colorDefaultId": "white green novelty leaves",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107524256",
			"colorsById": {
				"white green novelty leaves": {
					"id": "white green novelty leaves",
					"label": "WHITE GREEN NOVELTY LEAVES",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107524256",
						"13_107524253",
						"16_107524176"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "16_107524256"
				}
			},
			"colorIds": [
				"white green novelty leaves"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_107524253": {
					"id": "13_107524253",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107524253.jpg"
				},
				"16_107524176": {
					"id": "16_107524176",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107524176.jpg"
				},
				"16_107524256": {
					"id": "16_107524256",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107524256.jpg"
				}
			},
			"name": "1901 Slim Fit Leaf Print Short Sleeve Button-Down Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "29.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-slim-fit-leaf-print-short-sleeve-button-down-shirt/5447107",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5452806": {
			"id": 5452806,
			"brandId": 5155,
			"brandName": "ETON",
			"styleNumber": "5957377",
			"colorCount": 1,
			"colorDefaultId": "brown",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_106729089",
			"colorsById": {
				"brown": {
					"id": "brown",
					"label": "BROWN",
					"spriteIndex": 0,
					"mediaIds": [
						"9_106729089",
						"9_106733569",
						"12_106729092"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "9_106729089"
				}
			},
			"colorIds": [
				"brown"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_106729092": {
					"id": "12_106729092",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106729092.jpg"
				},
				"9_106729089": {
					"id": "9_106729089",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106729089.jpg"
				},
				"9_106733569": {
					"id": "9_106733569",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106733569.jpg"
				}
			},
			"name": "Eton Soft Casual Line Slim Fit Jersey Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "225.00",
					"maxItemPrice": "225.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "89.98",
					"maxItemPrice": "89.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/eton-soft-casual-line-slim-fit-jersey-shirt/5452806",
			"reviewCount": 2,
			"reviewStarRating": 3,
			"storeAvailability": null
		},
		"5453307": {
			"id": 5453307,
			"brandId": 783,
			"brandName": "WOOLRICH",
			"styleNumber": "5957822",
			"colorCount": 1,
			"colorDefaultId": "yellow",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_106655266",
			"colorsById": {
				"yellow": {
					"id": "yellow",
					"label": "YELLOW",
					"spriteIndex": 0,
					"mediaIds": [
						"6_106655266",
						"4_106655284",
						"19_106655279"
					],
					"standardColors": [
						"Yellow"
					],
					"swatchMediaId": "6_106655266"
				}
			},
			"colorIds": [
				"yellow"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"19_106655279": {
					"id": "19_106655279",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106655279.jpg"
				},
				"4_106655284": {
					"id": "4_106655284",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106655284.jpg"
				},
				"6_106655266": {
					"id": "6_106655266",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106655266.jpg"
				}
			},
			"name": "Woolrich Expedition Reversible Down Parka with Genuine Shearling Trim",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,400.00",
					"maxItemPrice": "1,400.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "560.00",
					"maxItemPrice": "560.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/woolrich-expedition-reversible-down-parka-with-genuine-shearling-trim/5453307",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5454992": {
			"id": 5454992,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5959230",
			"colorCount": 1,
			"colorDefaultId": "15 years mayhem",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_106801188",
			"colorsById": {
				"15 years mayhem": {
					"id": "15 years mayhem",
					"label": "15 YEARS MAYHEM",
					"spriteIndex": 0,
					"mediaIds": [
						"8_106801188",
						"7_106809807",
						"1_106809801"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_106801188"
				}
			},
			"colorIds": [
				"15 years mayhem"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"1_106809801": {
					"id": "1_106809801",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106809801.jpg"
				},
				"7_106809807": {
					"id": "7_106809807",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106809807.jpg"
				},
				"8_106801188": {
					"id": "8_106801188",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106801188.jpg"
				}
			},
			"name": "AG Tellis Slim Fit Jeans (15 Years Mayhem)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "225.00",
					"maxItemPrice": "225.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "157.50",
					"maxItemPrice": "157.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-tellis-slim-fit-jeans-15-years-mayhem/5454992",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5455956": {
			"id": 5455956,
			"brandId": 11896,
			"brandName": "BALENCIAGA",
			"styleNumber": "5960004",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_106796804",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"4_106796804",
						"5_106796805",
						"2_106796802"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "4_106796804"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"2_106796802": {
					"id": "2_106796802",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106796802.jpg"
				},
				"4_106796804": {
					"id": "4_106796804",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106796804.jpg"
				},
				"5_106796805": {
					"id": "5_106796805",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106796805.jpg"
				}
			},
			"name": "Balenciaga Logo Quilted Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "2,290.00",
					"maxItemPrice": "2,290.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "1,145.00",
					"maxItemPrice": "1,145.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/balenciaga-logo-quilted-bomber-jacket/5455956",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5471981": {
			"id": 5471981,
			"brandId": 320,
			"brandName": "BOSS HUGO BOSS",
			"styleNumber": "5970124",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=3_106964183",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"3_106964183",
						"1_106960741",
						"17_106960737"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "3_106964183"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"17_106960737": {
					"id": "17_106960737",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106960737.jpg"
				},
				"1_106960741": {
					"id": "1_106960741",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106960741.jpg"
				},
				"3_106964183": {
					"id": "3_106964183",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106964183.jpg"
				}
			},
			"name": "BOSS Huge/Genius Trim Fit Check Wool Suit",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "795.00",
					"maxItemPrice": "795.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 55,
					"maxItemPercentOff": 55,
					"minItemPrice": "357.75",
					"maxItemPrice": "357.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/boss-huge-genius-trim-fit-check-wool-suit/5471981",
			"reviewCount": 3,
			"reviewStarRating": 3.7,
			"storeAvailability": null
		},
		"5483545": {
			"id": 5483545,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "5978276",
			"colorCount": 2,
			"colorDefaultId": "blue textured knit",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107766921-15_107767075",
			"colorsById": {
				"blue textured knit": {
					"id": "blue textured knit",
					"label": "BLUE TEXTURED KNIT",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107766921",
						"12_107766952",
						"3_107766943"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_107766921"
				},
				"grey textured knit": {
					"id": "grey textured knit",
					"label": "GREY TEXTURED KNIT",
					"spriteIndex": 1,
					"mediaIds": [
						"15_107767075",
						"6_107767086",
						"3_107767083"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "15_107767075"
				}
			},
			"colorIds": [
				"blue textured knit",
				"grey textured knit"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107766952": {
					"id": "12_107766952",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107766952.jpg"
				},
				"15_107767075": {
					"id": "15_107767075",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107767075.jpg"
				},
				"1_107766921": {
					"id": "1_107766921",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107766921.jpg"
				},
				"3_107766943": {
					"id": "3_107766943",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107766943.jpg"
				},
				"3_107767083": {
					"id": "3_107767083",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107767083.jpg"
				},
				"6_107767086": {
					"id": "6_107767086",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107767086.jpg"
				}
			},
			"name": "Nordstrom Men's Shop X-Trim Fit Mélange Knit Sport Coat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "149.00",
					"maxItemPrice": "149.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-x-trim-fit-melange-knit-sport-coat/5483545",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5486677": {
			"id": 5486677,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5980259",
			"colorCount": 1,
			"colorDefaultId": "black white melange",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107575258",
			"colorsById": {
				"black white melange": {
					"id": "black white melange",
					"label": "BLACK WHITE MELANGE",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107575258",
						"7_107575267",
						"0_107575260"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_107575258"
				}
			},
			"colorIds": [
				"black white melange"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107575260": {
					"id": "0_107575260",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107575260.jpg"
				},
				"18_107575258": {
					"id": "18_107575258",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107575258.jpg"
				},
				"7_107575267": {
					"id": "7_107575267",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107575267.jpg"
				}
			},
			"name": "Zella Performance T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "20.00",
					"maxItemPrice": "20.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-performance-t-shirt/5486677",
			"reviewCount": 5,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5491027": {
			"id": 5491027,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "5982723",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107507536",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107507536",
						"8_107507528",
						"10_107507510"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "16_107507536"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107507510": {
					"id": "10_107507510",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107507510.jpg"
				},
				"16_107507536": {
					"id": "16_107507536",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107507536.jpg"
				},
				"8_107507528": {
					"id": "8_107507528",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107507528.jpg"
				}
			},
			"name": "BP. Ottoman Ribbed Sweater",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "29.00",
					"maxItemPrice": "29.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-ottoman-ribbed-sweater/5491027",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5491034": {
			"id": 5491034,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "5982725",
			"colorCount": 3,
			"colorDefaultId": "olive spice",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_107812335-3_107576683-2_107576702",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"3_107576683",
						"17_107576677",
						"2_107575822"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "3_107576683"
				},
				"grey heather": {
					"id": "grey heather",
					"label": "GREY HEATHER",
					"spriteIndex": 2,
					"mediaIds": [
						"2_107576702",
						"4_107576704",
						"17_107576697"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_107576702"
				},
				"olive spice": {
					"id": "olive spice",
					"label": "OLIVE SPICE",
					"spriteIndex": 0,
					"mediaIds": [
						"15_107812335",
						"11_107821911",
						"17_107811397"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "15_107812335"
				}
			},
			"colorIds": [
				"olive spice",
				"black",
				"grey heather"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107821911": {
					"id": "11_107821911",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107821911.jpg"
				},
				"15_107812335": {
					"id": "15_107812335",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107812335.jpg"
				},
				"17_107576677": {
					"id": "17_107576677",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107576677.jpg"
				},
				"17_107576697": {
					"id": "17_107576697",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107576697.jpg"
				},
				"17_107811397": {
					"id": "17_107811397",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107811397.jpg"
				},
				"2_107575822": {
					"id": "2_107575822",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107575822.jpg"
				},
				"2_107576702": {
					"id": "2_107576702",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107576702.jpg"
				},
				"3_107576683": {
					"id": "3_107576683",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107576683.jpg"
				},
				"4_107576704": {
					"id": "4_107576704",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107576704.jpg"
				}
			},
			"name": "BP. Ottoman Knit Drawstring Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "29.00",
					"maxItemPrice": "29.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-ottoman-knit-drawstring-shorts/5491034",
			"reviewCount": 3,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5492069": {
			"id": 5492069,
			"brandId": 7260,
			"brandName": "TRAVISMATHEW",
			"styleNumber": "5768331_1",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_105555075",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"15_105555075",
						"10_105565970",
						"7_106116547"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "15_105555075"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_105565970": {
					"id": "10_105565970",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_105565970.jpg"
				},
				"15_105555075": {
					"id": "15_105555075",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105555075.jpg"
				},
				"7_106116547": {
					"id": "7_106116547",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106116547.jpg"
				}
			},
			"name": "TravisMathew All In Performance Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "84.95",
					"maxItemPrice": "84.95",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "42.48",
					"maxItemPrice": "42.48",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/travismathew-all-in-performance-shorts/5492069",
			"reviewCount": 9,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5495874": {
			"id": 5495874,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5986388",
			"colorCount": 1,
			"colorDefaultId": "navy blazer flat floral",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=15_107711055",
			"colorsById": {
				"navy blazer flat floral": {
					"id": "navy blazer flat floral",
					"label": "NAVY BLAZER FLAT FLORAL",
					"spriteIndex": 0,
					"mediaIds": [
						"15_107711055",
						"19_107717799"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_107711055"
				}
			},
			"colorIds": [
				"navy blazer flat floral"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_107711055": {
					"id": "15_107711055",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107711055.jpg"
				},
				"19_107717799": {
					"id": "19_107717799",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107717799.jpg"
				}
			},
			"name": "1901 Spade Slim Fit Floral Short Sleeve Button-Down Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "29.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-spade-slim-fit-floral-short-sleeve-button-down-shirt/5495874",
			"reviewCount": 3,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5498077": {
			"id": 5498077,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "5987445",
			"colorCount": 4,
			"colorDefaultId": "blue feather mini paisley",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107770140-15_107770135-2_107770142-9_107770149",
			"colorsById": {
				"blue estate douglas plaid": {
					"id": "blue estate douglas plaid",
					"label": "BLUE ESTATE DOUGLAS PLAID",
					"spriteIndex": 1,
					"mediaIds": [
						"15_107770135",
						"16_107766036",
						"15_107766035"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_107770135"
				},
				"blue estate peter stripe": {
					"id": "blue estate peter stripe",
					"label": "BLUE ESTATE PETER STRIPE",
					"spriteIndex": 2,
					"mediaIds": [
						"2_107770142",
						"4_107766044",
						"3_107766043"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_107770142"
				},
				"blue feather mini paisley": {
					"id": "blue feather mini paisley",
					"label": "BLUE FEATHER MINI PAISLEY",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107770140",
						"0_107766040",
						"19_107766039"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_107770140"
				},
				"navy blazer nelson plaid": {
					"id": "navy blazer nelson plaid",
					"label": "NAVY BLAZER NELSON PLAID",
					"spriteIndex": 3,
					"mediaIds": [
						"9_107770149",
						"8_107766048",
						"7_107766047"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_107770149"
				}
			},
			"colorIds": [
				"blue feather mini paisley",
				"blue estate douglas plaid",
				"blue estate peter stripe",
				"navy blazer nelson plaid"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107766040": {
					"id": "0_107766040",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107766040.jpg"
				},
				"0_107770140": {
					"id": "0_107770140",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107770140.jpg"
				},
				"15_107766035": {
					"id": "15_107766035",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107766035.jpg"
				},
				"15_107770135": {
					"id": "15_107770135",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107770135.jpg"
				},
				"16_107766036": {
					"id": "16_107766036",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107766036.jpg"
				},
				"19_107766039": {
					"id": "19_107766039",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107766039.jpg"
				},
				"2_107770142": {
					"id": "2_107770142",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107770142.jpg"
				},
				"3_107766043": {
					"id": "3_107766043",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107766043.jpg"
				},
				"4_107766044": {
					"id": "4_107766044",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107766044.jpg"
				},
				"7_107766047": {
					"id": "7_107766047",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107766047.jpg"
				},
				"8_107766048": {
					"id": "8_107766048",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107766048.jpg"
				},
				"9_107770149": {
					"id": "9_107770149",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107770149.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Poplin Pajama Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.50",
					"maxItemPrice": "34.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-poplin-pajama-pants/5498077",
			"reviewCount": 6,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"5508608": {
			"id": 5508608,
			"brandId": 1354,
			"brandName": "DAVID DONAHUE",
			"styleNumber": "5994698",
			"colorCount": 1,
			"colorDefaultId": "blue",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_107463264",
			"colorsById": {
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 0,
					"mediaIds": [
						"4_107463264",
						"6_107463266"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "4_107463264"
				}
			},
			"colorIds": [
				"blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"4_107463264": {
					"id": "4_107463264",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107463264.jpg"
				},
				"6_107463266": {
					"id": "6_107463266",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107463266.jpg"
				}
			},
			"name": "David Donahue Trim Fit Floral Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "145.00",
					"maxItemPrice": "145.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 62,
					"maxItemPercentOff": 62,
					"minItemPrice": "54.98",
					"maxItemPrice": "54.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/david-donahue-trim-fit-floral-dress-shirt/5508608",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5514447": {
			"id": 5514447,
			"brandId": 7211,
			"brandName": "CARDINAL OF CANADA",
			"styleNumber": "5696603_1",
			"colorCount": 3,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_103831571-19_106561859-14_103831874",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_103831571",
						"14_104605114",
						"18_103831698"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "11_103831571"
				},
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 1,
					"mediaIds": [
						"19_106561859",
						"16_106534136",
						"14_106534134"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_106561859"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 2,
					"mediaIds": [
						"14_103831874",
						"18_103831878",
						"16_103831916"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_103831874"
				}
			},
			"colorIds": [
				"black",
				"charcoal",
				"navy"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_103831571": {
					"id": "11_103831571",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_103831571.jpg"
				},
				"14_103831874": {
					"id": "14_103831874",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_103831874.jpg"
				},
				"14_104605114": {
					"id": "14_104605114",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104605114.jpg"
				},
				"14_106534134": {
					"id": "14_106534134",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106534134.jpg"
				},
				"16_103831916": {
					"id": "16_103831916",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103831916.jpg"
				},
				"16_106534136": {
					"id": "16_106534136",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106534136.jpg"
				},
				"18_103831698": {
					"id": "18_103831698",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103831698.jpg"
				},
				"18_103831878": {
					"id": "18_103831878",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103831878.jpg"
				},
				"19_106561859": {
					"id": "19_106561859",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106561859.jpg"
				}
			},
			"name": "Cardinal of Canada Quilted Car Coat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "495.00",
					"maxItemPrice": "495.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "297.00",
					"maxItemPrice": "297.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cardinal-of-canada-quilted-car-coat/5514447",
			"reviewCount": 19,
			"reviewStarRating": 3.8,
			"storeAvailability": null
		},
		"5536516": {
			"id": 5536516,
			"brandId": 8111,
			"brandName": "BONOBOS",
			"styleNumber": "6009369",
			"colorCount": 1,
			"colorDefaultId": "blue and gold plaid",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107233581",
			"colorsById": {
				"blue and gold plaid": {
					"id": "blue and gold plaid",
					"label": "BLUE AND GOLD PLAID",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107233581",
						"7_107233587"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "1_107233581"
				}
			},
			"colorIds": [
				"blue and gold plaid"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"1_107233581": {
					"id": "1_107233581",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107233581.jpg"
				},
				"7_107233587": {
					"id": "7_107233587",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107233587.jpg"
				}
			},
			"name": "Bonobos Slim Fit Plaid Unconstructed Wool Blazer",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "450.00",
					"maxItemPrice": "450.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "180.00",
					"maxItemPrice": "180.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bonobos-slim-fit-plaid-unconstructed-wool-blazer/5536516",
			"reviewCount": 3,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5543362": {
			"id": 5543362,
			"brandId": 5155,
			"brandName": "ETON",
			"styleNumber": "6013345",
			"colorCount": 2,
			"colorDefaultId": "purple",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107361778-2_107361782",
			"colorsById": {
				"blue": {
					"id": "blue",
					"label": "BLUE",
					"spriteIndex": 1,
					"mediaIds": [
						"2_107361782",
						"6_107355846",
						"0_107361780"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_107361782"
				},
				"purple": {
					"id": "purple",
					"label": "PURPLE",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107361778",
						"6_107355866",
						"13_107361773"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "18_107361778"
				}
			},
			"colorIds": [
				"purple",
				"blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107361780": {
					"id": "0_107361780",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107361780.jpg"
				},
				"13_107361773": {
					"id": "13_107361773",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107361773.jpg"
				},
				"18_107361778": {
					"id": "18_107361778",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107361778.jpg"
				},
				"2_107361782": {
					"id": "2_107361782",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107361782.jpg"
				},
				"6_107355846": {
					"id": "6_107355846",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107355846.jpg"
				},
				"6_107355866": {
					"id": "6_107355866",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107355866.jpg"
				}
			},
			"name": "Eton Contemporary Fit Check Dress Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "285.00",
					"maxItemPrice": "285.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 61,
					"maxItemPercentOff": 61,
					"minItemPrice": "109.98",
					"maxItemPrice": "109.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/eton-contemporary-fit-check-dress-shirt/5543362",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5544377": {
			"id": 5544377,
			"brandId": 12921,
			"brandName": "GOODLIFE",
			"styleNumber": "5242585_1",
			"colorCount": 4,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_106309359-12_106309392-10_106309430-8_105029128",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"19_106309359",
						"19_106309379",
						"13_106309453"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "19_106309359"
				},
				"goodlife navy": {
					"id": "goodlife navy",
					"label": "GOODLIFE NAVY",
					"spriteIndex": 1,
					"mediaIds": [
						"12_106309392",
						"5_106309425",
						"13_106309453"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_106309392"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"10_106309430",
						"15_106309455",
						"13_106309453"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "10_106309430"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 3,
					"mediaIds": [
						"8_105029128",
						"4_13160044",
						"13_106309453"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "8_105029128"
				}
			},
			"colorIds": [
				"black",
				"goodlife navy",
				"heather grey",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106309430": {
					"id": "10_106309430",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106309430.jpg"
				},
				"12_106309392": {
					"id": "12_106309392",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106309392.jpg"
				},
				"13_106309453": {
					"id": "13_106309453",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106309453.jpg"
				},
				"15_106309455": {
					"id": "15_106309455",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106309455.jpg"
				},
				"19_106309359": {
					"id": "19_106309359",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106309359.jpg"
				},
				"19_106309379": {
					"id": "19_106309379",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106309379.jpg"
				},
				"4_13160044": {
					"id": "4_13160044",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_13160044.jpg"
				},
				"5_106309425": {
					"id": "5_106309425",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106309425.jpg"
				},
				"8_105029128": {
					"id": "8_105029128",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_105029128.jpg"
				}
			},
			"name": "Goodlife Triblend Scallop Long Sleeve Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "75.00",
					"maxItemPrice": "75.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/goodlife-triblend-scallop-long-sleeve-crewneck-t-shirt/5544377",
			"reviewCount": 15,
			"reviewStarRating": 4.1,
			"storeAvailability": null
		},
		"5544389": {
			"id": 5544389,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5301210_13",
			"colorCount": 4,
			"colorDefaultId": "blue white bengal stripe",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_105936182-9_103354049-18_102990118-17_103352497",
			"colorsById": {
				"blue dusk oxford": {
					"id": "blue dusk oxford",
					"label": "BLUE DUSK OXFORD",
					"spriteIndex": 1,
					"mediaIds": [
						"9_103354049",
						"5_103354045",
						"3_103352463"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "9_103354049"
				},
				"blue white bengal stripe": {
					"id": "blue white bengal stripe",
					"label": "BLUE WHITE BENGAL STRIPE",
					"spriteIndex": 0,
					"mediaIds": [
						"2_105936182",
						"7_105936187",
						"17_105935997"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_105936182"
				},
				"grey magnet oxford": {
					"id": "grey magnet oxford",
					"label": "GREY MAGNET OXFORD",
					"spriteIndex": 2,
					"mediaIds": [
						"18_102990118",
						"4_102990124",
						"11_102988631"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_102990118"
				},
				"white oxford": {
					"id": "white oxford",
					"label": "WHITE OXFORD",
					"spriteIndex": 3,
					"mediaIds": [
						"17_103352497",
						"16_103352496",
						"10_103352470"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "17_103352497"
				}
			},
			"colorIds": [
				"blue white bengal stripe",
				"blue dusk oxford",
				"grey magnet oxford",
				"white oxford"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_103352470": {
					"id": "10_103352470",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_103352470.jpg"
				},
				"11_102988631": {
					"id": "11_102988631",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_102988631.jpg"
				},
				"16_103352496": {
					"id": "16_103352496",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103352496.jpg"
				},
				"17_103352497": {
					"id": "17_103352497",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_103352497.jpg"
				},
				"17_105935997": {
					"id": "17_105935997",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105935997.jpg"
				},
				"18_102990118": {
					"id": "18_102990118",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_102990118.jpg"
				},
				"2_105936182": {
					"id": "2_105936182",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_105936182.jpg"
				},
				"3_103352463": {
					"id": "3_103352463",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_103352463.jpg"
				},
				"4_102990124": {
					"id": "4_102990124",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_102990124.jpg"
				},
				"5_103354045": {
					"id": "5_103354045",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_103354045.jpg"
				},
				"7_105936187": {
					"id": "7_105936187",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105936187.jpg"
				},
				"9_103354049": {
					"id": "9_103354049",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_103354049.jpg"
				}
			},
			"name": "1901 Trim Fit Washed Oxford Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "49.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.90",
					"maxItemPrice": "29.90",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-trim-fit-washed-oxford-shirt/5544389",
			"reviewCount": 28,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5557704": {
			"id": 5557704,
			"brandId": 9512,
			"brandName": "FAHERTY BRAND",
			"styleNumber": "6022764",
			"colorCount": 4,
			"colorDefaultId": "charcoal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_107119802-17_107114317-10_107120410-2_107110482",
			"colorsById": {
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 0,
					"mediaIds": [
						"2_107119802",
						"14_107121894",
						"17_107121877"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "2_107119802"
				},
				"ice grey": {
					"id": "ice grey",
					"label": "ICE GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"17_107114317",
						"5_107120225",
						"19_107114319"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "17_107114317"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 2,
					"mediaIds": [
						"10_107120410",
						"10_107140590",
						"19_107120459"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "10_107120410"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"2_107110482",
						"0_107120240",
						"9_107110689"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_107110482"
				}
			},
			"colorIds": [
				"charcoal",
				"ice grey",
				"khaki",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107120240": {
					"id": "0_107120240",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107120240.jpg"
				},
				"10_107120410": {
					"id": "10_107120410",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107120410.jpg"
				},
				"10_107140590": {
					"id": "10_107140590",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107140590.jpg"
				},
				"14_107121894": {
					"id": "14_107121894",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107121894.jpg"
				},
				"17_107114317": {
					"id": "17_107114317",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107114317.jpg"
				},
				"17_107121877": {
					"id": "17_107121877",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107121877.jpg"
				},
				"19_107114319": {
					"id": "19_107114319",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107114319.jpg"
				},
				"19_107120459": {
					"id": "19_107120459",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107120459.jpg"
				},
				"2_107110482": {
					"id": "2_107110482",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107110482.jpg"
				},
				"2_107119802": {
					"id": "2_107119802",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107119802.jpg"
				},
				"5_107120225": {
					"id": "5_107120225",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107120225.jpg"
				},
				"9_107110689": {
					"id": "9_107110689",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107110689.jpg"
				}
			},
			"name": "Faherty All Day Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/faherty-all-day-shorts/5557704",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5561725": {
			"id": 5561725,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "5642998_1",
			"colorCount": 1,
			"colorDefaultId": "grey marl",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_106354311",
			"colorsById": {
				"grey marl": {
					"id": "grey marl",
					"label": "GREY MARL",
					"spriteIndex": 0,
					"mediaIds": [
						"11_106354311",
						"5_106354325",
						"4_106354384"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "11_106354311"
				}
			},
			"colorIds": [
				"grey marl"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_106354311": {
					"id": "11_106354311",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106354311.jpg"
				},
				"4_106354384": {
					"id": "4_106354384",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106354384.jpg"
				},
				"5_106354325": {
					"id": "5_106354325",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106354325.jpg"
				}
			},
			"name": "ALLSAINTS Mode Slim Fit Wool Cardigan",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "120.00",
					"maxItemPrice": "120.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "84.00",
					"maxItemPrice": "84.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-mode-slim-fit-wool-cardigan/5561725",
			"reviewCount": 2,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5572356": {
			"id": 5572356,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "6032924",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107383172",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107383172",
						"16_107383176",
						"15_107383175"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_107383172"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107383172": {
					"id": "12_107383172",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107383172.jpg"
				},
				"15_107383175": {
					"id": "15_107383175",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107383175.jpg"
				},
				"16_107383176": {
					"id": "16_107383176",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107383176.jpg"
				}
			},
			"name": "ALLSAINTS Bassett Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "198.00",
					"maxItemPrice": "198.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-bassett-bomber-jacket/5572356",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5574127": {
			"id": 5574127,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "6034483",
			"colorCount": 1,
			"colorDefaultId": "4 years decode",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_107205650",
			"colorsById": {
				"4 years decode": {
					"id": "4 years decode",
					"label": "4 YEARS DECODE",
					"spriteIndex": 0,
					"mediaIds": [
						"10_107205650",
						"5_107223805",
						"2_107223802"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_107205650"
				}
			},
			"colorIds": [
				"4 years decode"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107205650": {
					"id": "10_107205650",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107205650.jpg"
				},
				"2_107223802": {
					"id": "2_107223802",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107223802.jpg"
				},
				"5_107223805": {
					"id": "5_107223805",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107223805.jpg"
				}
			},
			"name": "AG Graduate Slim Straight Leg Jeans (4 Years Decode)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "215.00",
					"maxItemPrice": "215.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "107.50",
					"maxItemPrice": "107.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-graduate-slim-straight-leg-jeans-4-years-decode/5574127",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5581440": {
			"id": 5581440,
			"brandId": 11669,
			"brandName": "MADEWELL",
			"styleNumber": "6040307",
			"colorCount": 4,
			"colorDefaultId": "sage mist",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_107712019-16_107485596-7_107712027-5_107712005",
			"colorsById": {
				"autumn meadow": {
					"id": "autumn meadow",
					"label": "AUTUMN MEADOW",
					"spriteIndex": 1,
					"mediaIds": [
						"16_107485596",
						"17_107485597"
					],
					"standardColors": [
						"Offwhite"
					],
					"swatchMediaId": "16_107485596"
				},
				"black coal": {
					"id": "black coal",
					"label": "BLACK COAL",
					"spriteIndex": 2,
					"mediaIds": [
						"7_107712027",
						"4_107692924"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "7_107712027"
				},
				"nighttime": {
					"id": "nighttime",
					"label": "NIGHTTIME",
					"spriteIndex": 3,
					"mediaIds": [
						"5_107712005",
						"9_107692929"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107712005"
				},
				"sage mist": {
					"id": "sage mist",
					"label": "SAGE MIST",
					"spriteIndex": 0,
					"mediaIds": [
						"19_107712019",
						"19_107713619"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "19_107712019"
				}
			},
			"colorIds": [
				"sage mist",
				"autumn meadow",
				"black coal",
				"nighttime"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_107485596": {
					"id": "16_107485596",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107485596.jpg"
				},
				"17_107485597": {
					"id": "17_107485597",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107485597.jpg"
				},
				"19_107712019": {
					"id": "19_107712019",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107712019.jpg"
				},
				"19_107713619": {
					"id": "19_107713619",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107713619.jpg"
				},
				"4_107692924": {
					"id": "4_107692924",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107692924.jpg"
				},
				"5_107712005": {
					"id": "5_107712005",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107712005.jpg"
				},
				"7_107712027": {
					"id": "7_107712027",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107712027.jpg"
				},
				"9_107692929": {
					"id": "9_107692929",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107692929.jpg"
				}
			},
			"name": "Madewell Everywear Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/madewell-everywear-shorts/5581440",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5586475": {
			"id": 5586475,
			"brandId": 320,
			"brandName": "BOSS HUGO BOSS",
			"styleNumber": "5878057_1",
			"colorCount": 1,
			"colorDefaultId": "teal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107009232",
			"colorsById": {
				"teal": {
					"id": "teal",
					"label": "TEAL",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107009232",
						"15_107009375",
						"3_107009323"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_107009232"
				}
			},
			"colorIds": [
				"teal"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107009232": {
					"id": "12_107009232",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107009232.jpg"
				},
				"15_107009375": {
					"id": "15_107009375",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107009375.jpg"
				},
				"3_107009323": {
					"id": "3_107009323",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107009323.jpg"
				}
			},
			"name": "BOSS Parlay 78 Solid Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "128.00",
					"maxItemPrice": "128.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "64.00",
					"maxItemPrice": "64.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/boss-parlay-78-solid-polo/5586475",
			"reviewCount": 6,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5590762": {
			"id": 5590762,
			"brandId": 7260,
			"brandName": "TRAVISMATHEW",
			"styleNumber": "6046320",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107681901",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107681901",
						"5_107688005",
						"3_107688003"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "1_107681901"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"1_107681901": {
					"id": "1_107681901",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107681901.jpg"
				},
				"3_107688003": {
					"id": "3_107688003",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107688003.jpg"
				},
				"5_107688005": {
					"id": "5_107688005",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107688005.jpg"
				}
			},
			"name": "TravisMathew Nosedive Short Sleeve Button-Up Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "94.95",
					"maxItemPrice": "94.95",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/travismathew-nosedive-short-sleeve-button-up-shirt/5590762",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5593394": {
			"id": 5593394,
			"brandId": 21261,
			"brandName": "NOAH",
			"styleNumber": "6047824",
			"colorCount": 1,
			"colorDefaultId": "multi",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_107673945",
			"colorsById": {
				"multi": {
					"id": "multi",
					"label": "MULTI",
					"spriteIndex": 0,
					"mediaIds": [
						"5_107673945",
						"7_107674447",
						"18_107702198"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107673945"
				}
			},
			"colorIds": [
				"multi"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"18_107702198": {
					"id": "18_107702198",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107702198.jpg"
				},
				"5_107673945": {
					"id": "5_107673945",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107673945.jpg"
				},
				"7_107674447": {
					"id": "7_107674447",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107674447.jpg"
				}
			},
			"name": "Noah x Birdwell 310 Colorblock Boardshorts (Nordstrom Exclusive)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "120.00",
					"maxItemPrice": "120.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/noah-x-birdwell-310-colorblock-boardshorts-nordstrom-exclusive/5593394",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5593430": {
			"id": 5593430,
			"brandId": 21261,
			"brandName": "NOAH",
			"styleNumber": "6047879",
			"colorCount": 8,
			"colorDefaultId": "island reef",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_107693725-1_107671601-12_107693732-8_107693728-12_107671612-10_107671610-8_107671608-9_107693729",
			"colorsById": {
				"banana": {
					"id": "banana",
					"label": "BANANA",
					"spriteIndex": 1,
					"mediaIds": [
						"1_107671601",
						"19_107670599",
						"8_107700608"
					],
					"standardColors": [
						"Yellow"
					],
					"swatchMediaId": "1_107671601"
				},
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 2,
					"mediaIds": [
						"12_107693732",
						"12_107692912",
						"3_107701703"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "12_107693732"
				},
				"boysenberry": {
					"id": "boysenberry",
					"label": "BOYSENBERRY",
					"spriteIndex": 3,
					"mediaIds": [
						"8_107693728",
						"4_107692944",
						"1_107701501"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "8_107693728"
				},
				"island reef": {
					"id": "island reef",
					"label": "ISLAND REEF",
					"spriteIndex": 0,
					"mediaIds": [
						"5_107693725",
						"13_107692953",
						"4_107701504"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107693725"
				},
				"orchid": {
					"id": "orchid",
					"label": "ORCHID",
					"spriteIndex": 4,
					"mediaIds": [
						"12_107671612",
						"18_107670618",
						"5_107701105"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "12_107671612"
				},
				"pepper": {
					"id": "pepper",
					"label": "PEPPER",
					"spriteIndex": 5,
					"mediaIds": [
						"10_107671610",
						"13_107670613",
						"9_107701569"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "10_107671610"
				},
				"true navy": {
					"id": "true navy",
					"label": "TRUE NAVY",
					"spriteIndex": 6,
					"mediaIds": [
						"8_107671608",
						"7_107670607",
						"16_107702216"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_107671608"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 7,
					"mediaIds": [
						"9_107693729",
						"8_107692928",
						"12_107701452"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "9_107693729"
				}
			},
			"colorIds": [
				"island reef",
				"banana",
				"black",
				"boysenberry",
				"orchid",
				"pepper",
				"true navy",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107671610": {
					"id": "10_107671610",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107671610.jpg"
				},
				"12_107671612": {
					"id": "12_107671612",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107671612.jpg"
				},
				"12_107692912": {
					"id": "12_107692912",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107692912.jpg"
				},
				"12_107693732": {
					"id": "12_107693732",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107693732.jpg"
				},
				"12_107701452": {
					"id": "12_107701452",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107701452.jpg"
				},
				"13_107670613": {
					"id": "13_107670613",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107670613.jpg"
				},
				"13_107692953": {
					"id": "13_107692953",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107692953.jpg"
				},
				"16_107702216": {
					"id": "16_107702216",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107702216.jpg"
				},
				"18_107670618": {
					"id": "18_107670618",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107670618.jpg"
				},
				"19_107670599": {
					"id": "19_107670599",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107670599.jpg"
				},
				"1_107671601": {
					"id": "1_107671601",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107671601.jpg"
				},
				"1_107701501": {
					"id": "1_107701501",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107701501.jpg"
				},
				"3_107701703": {
					"id": "3_107701703",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107701703.jpg"
				},
				"4_107692944": {
					"id": "4_107692944",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107692944.jpg"
				},
				"4_107701504": {
					"id": "4_107701504",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107701504.jpg"
				},
				"5_107693725": {
					"id": "5_107693725",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107693725.jpg"
				},
				"5_107701105": {
					"id": "5_107701105",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107701105.jpg"
				},
				"7_107670607": {
					"id": "7_107670607",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107670607.jpg"
				},
				"8_107671608": {
					"id": "8_107671608",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107671608.jpg"
				},
				"8_107692928": {
					"id": "8_107692928",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107692928.jpg"
				},
				"8_107693728": {
					"id": "8_107693728",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107693728.jpg"
				},
				"8_107700608": {
					"id": "8_107700608",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107700608.jpg"
				},
				"9_107693729": {
					"id": "9_107693729",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107693729.jpg"
				},
				"9_107701569": {
					"id": "9_107701569",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107701569.jpg"
				}
			},
			"name": "Noah Core Logo Pocket T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "52.00",
					"maxItemPrice": "52.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/noah-core-logo-pocket-t-shirt/5593430",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5595816": {
			"id": 5595816,
			"brandId": 5160,
			"brandName": "VINEYARD VINES",
			"styleNumber": "6049626",
			"colorCount": 1,
			"colorDefaultId": "turqs",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107726360",
			"colorsById": {
				"turqs": {
					"id": "turqs",
					"label": "TURQS",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107726360",
						"6_107724106",
						"5_107724105"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "0_107726360"
				}
			},
			"colorIds": [
				"turqs"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107726360": {
					"id": "0_107726360",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107726360.jpg"
				},
				"5_107724105": {
					"id": "5_107724105",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107724105.jpg"
				},
				"6_107724106": {
					"id": "6_107724106",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107724106.jpg"
				}
			},
			"name": "vineyard vines Sandbar Slim Fit Button-Down Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "115.00",
					"maxItemPrice": "115.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vineyard-vines-sandbar-slim-fit-button-down-shirt/5595816",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5602849": {
			"id": 5602849,
			"brandId": 5289,
			"brandName": "GIRAFFE AT HOME",
			"styleNumber": "6053927",
			"colorCount": 4,
			"colorDefaultId": "charcoal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=1_107638001-2_107440302-0_107440300-18_107440298",
			"colorsById": {
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 0,
					"mediaIds": [
						"1_107638001",
						"4_107440304"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "1_107638001"
				},
				"cream": {
					"id": "cream",
					"label": "CREAM",
					"spriteIndex": 1,
					"mediaIds": [
						"2_107440302",
						"3_107440303"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "2_107440302"
				},
				"onyx": {
					"id": "onyx",
					"label": "ONYX",
					"spriteIndex": 2,
					"mediaIds": [
						"0_107440300",
						"1_107440301"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_107440300"
				},
				"silver": {
					"id": "silver",
					"label": "SILVER",
					"spriteIndex": 3,
					"mediaIds": [
						"18_107440298",
						"19_107440299"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_107440298"
				}
			},
			"colorIds": [
				"charcoal",
				"cream",
				"onyx",
				"silver"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107440300": {
					"id": "0_107440300",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107440300.jpg"
				},
				"18_107440298": {
					"id": "18_107440298",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107440298.jpg"
				},
				"19_107440299": {
					"id": "19_107440299",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107440299.jpg"
				},
				"1_107440301": {
					"id": "1_107440301",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107440301.jpg"
				},
				"1_107638001": {
					"id": "1_107638001",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107638001.jpg"
				},
				"2_107440302": {
					"id": "2_107440302",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107440302.jpg"
				},
				"3_107440303": {
					"id": "3_107440303",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107440303.jpg"
				},
				"4_107440304": {
					"id": "4_107440304",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107440304.jpg"
				}
			},
			"name": "Giraffe at Home Dolce Chenille Hooded Robe",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "167.00",
					"maxItemPrice": "167.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/giraffe-at-home-dolce-chenille-hooded-robe/5602849",
			"reviewCount": 3,
			"reviewStarRating": 3,
			"storeAvailability": null
		},
		"5607508": {
			"id": 5607508,
			"brandId": 320,
			"brandName": "BOSS HUGO BOSS",
			"styleNumber": "6057095",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_107675073",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"13_107675073",
						"17_107674917",
						"19_107674919"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_107675073"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_107675073": {
					"id": "13_107675073",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107675073.jpg"
				},
				"17_107674917": {
					"id": "17_107674917",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107674917.jpg"
				},
				"19_107674919": {
					"id": "19_107674919",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107674919.jpg"
				}
			},
			"name": "BOSS Shepherd Knit Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "178.00",
					"maxItemPrice": "178.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/boss-shepherd-knit-bomber-jacket/5607508",
			"reviewCount": 2,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5608448": {
			"id": 5608448,
			"brandId": 9226,
			"brandName": "RODD AND GUNN",
			"styleNumber": "6057800",
			"colorCount": 1,
			"colorDefaultId": "coffee",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_107563991",
			"colorsById": {
				"coffee": {
					"id": "coffee",
					"label": "COFFEE",
					"spriteIndex": 0,
					"mediaIds": [
						"11_107563991",
						"18_107563998",
						"13_107563993"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "11_107563991"
				}
			},
			"colorIds": [
				"coffee"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107563991": {
					"id": "11_107563991",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107563991.jpg"
				},
				"13_107563993": {
					"id": "13_107563993",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107563993.jpg"
				},
				"18_107563998": {
					"id": "18_107563998",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107563998.jpg"
				}
			},
			"name": "Rodd & Gunn Lake Hawea Suede Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "798.00",
					"maxItemPrice": "798.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/rodd-gunn-lake-hawea-suede-bomber-jacket/5608448",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5608596": {
			"id": 5608596,
			"brandId": 19481,
			"brandName": "NOON GOONS",
			"styleNumber": "6057921",
			"colorCount": 2,
			"colorDefaultId": "green",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_107671064-10_107671150",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"10_107671150",
						"18_107671158",
						"17_107671157"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_107671150"
				},
				"green": {
					"id": "green",
					"label": "GREEN",
					"spriteIndex": 0,
					"mediaIds": [
						"4_107671064",
						"2_107671082",
						"18_107671078"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "4_107671064"
				}
			},
			"colorIds": [
				"green",
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107671150": {
					"id": "10_107671150",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107671150.jpg"
				},
				"17_107671157": {
					"id": "17_107671157",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107671157.jpg"
				},
				"18_107671078": {
					"id": "18_107671078",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107671078.jpg"
				},
				"18_107671158": {
					"id": "18_107671158",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107671158.jpg"
				},
				"2_107671082": {
					"id": "2_107671082",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107671082.jpg"
				},
				"4_107671064": {
					"id": "4_107671064",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107671064.jpg"
				}
			},
			"name": "Noon Goons Team Water Resistant Coach's Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "119.99",
					"maxItemPrice": "119.99",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "71.99",
					"maxItemPrice": "71.99",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/noon-goons-team-water-resistant-coachs-jacket/5608596",
			"reviewCount": 1,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5614097": {
			"id": 5614097,
			"brandId": 6151,
			"brandName": "PSYCHO BUNNY",
			"styleNumber": "6061821",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_107840311",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_107840311",
						"15_107840295",
						"13_107840293"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "11_107840311"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107840311": {
					"id": "11_107840311",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107840311.jpg"
				},
				"13_107840293": {
					"id": "13_107840293",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107840293.jpg"
				},
				"15_107840295": {
					"id": "15_107840295",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107840295.jpg"
				}
			},
			"name": "Psycho Bunny Arlington Piqué Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/psycho-bunny-arlington-pique-polo/5614097",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5614099": {
			"id": 5614099,
			"brandId": 6151,
			"brandName": "PSYCHO BUNNY",
			"styleNumber": "6061825",
			"colorCount": 3,
			"colorDefaultId": "668 camelia",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107842112-19_107842119-17_107842117",
			"colorsById": {
				"442 belair": {
					"id": "442 belair",
					"label": "442 BELAIR",
					"spriteIndex": 1,
					"mediaIds": [
						"19_107842119",
						"15_107809075"
					],
					"standardColors": [
						"Blue",
						"Green"
					],
					"swatchMediaId": "19_107842119"
				},
				"668 camelia": {
					"id": "668 camelia",
					"label": "668 CAMELIA",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107842112",
						"1_107843921"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "12_107842112"
				},
				"853 flange": {
					"id": "853 flange",
					"label": "853 FLANGE",
					"spriteIndex": 2,
					"mediaIds": [
						"17_107842117",
						"4_107809064"
					],
					"standardColors": [
						"Orange"
					],
					"swatchMediaId": "17_107842117"
				}
			},
			"colorIds": [
				"668 camelia",
				"442 belair",
				"853 flange"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107842112": {
					"id": "12_107842112",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107842112.jpg"
				},
				"15_107809075": {
					"id": "15_107809075",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107809075.jpg"
				},
				"17_107842117": {
					"id": "17_107842117",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107842117.jpg"
				},
				"19_107842119": {
					"id": "19_107842119",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107842119.jpg"
				},
				"1_107843921": {
					"id": "1_107843921",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107843921.jpg"
				},
				"4_107809064": {
					"id": "4_107809064",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107809064.jpg"
				}
			},
			"name": "Psycho Bunny Bower Tipped Short Sleeve Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/psycho-bunny-bower-tipped-short-sleeve-polo/5614099",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5615453": {
			"id": 5615453,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "6063198",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=5_107685025",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"5_107685025",
						"19_107690859",
						"17_107690857"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "5_107685025"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"17_107690857": {
					"id": "17_107690857",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107690857.jpg"
				},
				"19_107690859": {
					"id": "19_107690859",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107690859.jpg"
				},
				"5_107685025": {
					"id": "5_107685025",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107685025.jpg"
				}
			},
			"name": "ALLSAINTS Vieno Leather Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "498.00",
					"maxItemPrice": "498.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-vieno-leather-jacket/5615453",
			"reviewCount": 4,
			"reviewStarRating": 3,
			"storeAvailability": null
		},
		"5615463": {
			"id": 5615463,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "6063204",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_107639927",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"7_107639927",
						"0_107643620",
						"19_107643619"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "7_107639927"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107643620": {
					"id": "0_107643620",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107643620.jpg"
				},
				"19_107643619": {
					"id": "19_107643619",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107643619.jpg"
				},
				"7_107639927": {
					"id": "7_107639927",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107639927.jpg"
				}
			},
			"name": "ALLSAINTS Udan Slim Fit Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "198.00",
					"maxItemPrice": "198.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-udan-slim-fit-bomber-jacket/5615463",
			"reviewCount": 3,
			"reviewStarRating": 2.7,
			"storeAvailability": null
		},
		"5619519": {
			"id": 5619519,
			"brandId": 4883,
			"brandName": "KENZO",
			"styleNumber": "6065841",
			"colorCount": 2,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_107568142-19_107568119",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"2_107568142",
						"4_107568144"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "2_107568142"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 1,
					"mediaIds": [
						"19_107568119",
						"2_107568122"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "19_107568119"
				}
			},
			"colorIds": [
				"black",
				"white"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"19_107568119": {
					"id": "19_107568119",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107568119.jpg"
				},
				"2_107568122": {
					"id": "2_107568122",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107568122.jpg"
				},
				"2_107568142": {
					"id": "2_107568142",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107568142.jpg"
				},
				"4_107568144": {
					"id": "4_107568144",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107568144.jpg"
				}
			},
			"name": "KENZO Classic Tiger Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "135.00",
					"maxItemPrice": "135.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/kenzo-classic-tiger-graphic-tee/5619519",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5628365": {
			"id": 5628365,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "6071413",
			"colorCount": 1,
			"colorDefaultId": "silver holographic",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_107596186",
			"colorsById": {
				"silver holographic": {
					"id": "silver holographic",
					"label": "SILVER HOLOGRAPHIC",
					"spriteIndex": 0,
					"mediaIds": [
						"6_107596186",
						"5_107596185",
						"4_107596184"
					],
					"standardColors": [
						"Metallic"
					],
					"swatchMediaId": "6_107596186"
				}
			},
			"colorIds": [
				"silver holographic"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"4_107596184": {
					"id": "4_107596184",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107596184.jpg"
				},
				"5_107596185": {
					"id": "5_107596185",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107596185.jpg"
				},
				"6_107596186": {
					"id": "6_107596186",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107596186.jpg"
				}
			},
			"name": "BP. Be Proud by BP. Gender Inclusive Holographic Skirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "29.00",
					"maxItemPrice": "29.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "17.40",
					"maxItemPrice": "17.40",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-be-proud-by-bp-gender-inclusive-holographic-skirt/5628365",
			"reviewCount": 8,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5628368": {
			"id": 5628368,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "6071416",
			"colorCount": 1,
			"colorDefaultId": "blue multi tie dye print",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=8_107615848",
			"colorsById": {
				"blue multi tie dye print": {
					"id": "blue multi tie dye print",
					"label": "BLUE MULTI TIE DYE PRINT",
					"spriteIndex": 0,
					"mediaIds": [
						"8_107615848",
						"7_107615847",
						"13_107615553"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "8_107615848"
				}
			},
			"colorIds": [
				"blue multi tie dye print"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_107615553": {
					"id": "13_107615553",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107615553.jpg"
				},
				"7_107615847": {
					"id": "7_107615847",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107615847.jpg"
				},
				"8_107615848": {
					"id": "8_107615848",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107615848.jpg"
				}
			},
			"name": "BP. Be Proud by BP. Gender Inclusive Tie Dye Tunic Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "65.00",
					"maxItemPrice": "65.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-be-proud-by-bp-gender-inclusive-tie-dye-tunic-hoodie/5628368",
			"reviewCount": 1,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5628369": {
			"id": 5628369,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "6071417",
			"colorCount": 1,
			"colorDefaultId": "pink multi tie dye",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_107596146",
			"colorsById": {
				"pink multi tie dye": {
					"id": "pink multi tie dye",
					"label": "PINK MULTI TIE DYE",
					"spriteIndex": 0,
					"mediaIds": [
						"6_107596146",
						"4_107596144"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "6_107596146"
				}
			},
			"colorIds": [
				"pink multi tie dye"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"4_107596144": {
					"id": "4_107596144",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107596144.jpg"
				},
				"6_107596146": {
					"id": "6_107596146",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107596146.jpg"
				}
			},
			"name": "BP. Be Proud by BP. Gender Inclusive Tie-Dye Mesh Turtleneck",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.00",
					"maxItemPrice": "39.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "23.40",
					"maxItemPrice": "23.40",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-be-proud-by-bp-gender-inclusive-tie-dye-mesh-turtleneck/5628369",
			"reviewCount": 3,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5628371": {
			"id": 5628371,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "6071419",
			"colorCount": 2,
			"colorDefaultId": "pink begonia",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107595978-8_107595128",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"8_107595128",
						"7_107595127",
						"11_107595131"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "8_107595128"
				},
				"pink begonia": {
					"id": "pink begonia",
					"label": "PINK BEGONIA",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107595978",
						"17_107595977",
						"8_107595968"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "18_107595978"
				}
			},
			"colorIds": [
				"pink begonia",
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107595131": {
					"id": "11_107595131",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107595131.jpg"
				},
				"17_107595977": {
					"id": "17_107595977",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107595977.jpg"
				},
				"18_107595978": {
					"id": "18_107595978",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107595978.jpg"
				},
				"7_107595127": {
					"id": "7_107595127",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107595127.jpg"
				},
				"8_107595128": {
					"id": "8_107595128",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107595128.jpg"
				},
				"8_107595968": {
					"id": "8_107595968",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107595968.jpg"
				}
			},
			"name": "BP. Be Proud by BP. Gender Inclusive Athletic Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "39.00",
					"maxItemPrice": "39.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "23.40",
					"maxItemPrice": "23.40",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-be-proud-by-bp-gender-inclusive-athletic-shorts/5628371",
			"reviewCount": 5,
			"reviewStarRating": 3.2,
			"storeAvailability": null
		},
		"5628373": {
			"id": 5628373,
			"brandId": 814,
			"brandName": "BP",
			"styleNumber": "6071421",
			"colorCount": 2,
			"colorDefaultId": "green punch",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_107596213-1_107595961",
			"colorsById": {
				"green punch": {
					"id": "green punch",
					"label": "GREEN PUNCH",
					"spriteIndex": 0,
					"mediaIds": [
						"13_107596213",
						"12_107596212",
						"5_107596205"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "13_107596213"
				},
				"pink faded butterfly": {
					"id": "pink faded butterfly",
					"label": "PINK FADED BUTTERFLY",
					"spriteIndex": 1,
					"mediaIds": [
						"1_107595961",
						"0_107595960",
						"15_107595955"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "1_107595961"
				}
			},
			"colorIds": [
				"green punch",
				"pink faded butterfly"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107595960": {
					"id": "0_107595960",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107595960.jpg"
				},
				"12_107596212": {
					"id": "12_107596212",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107596212.jpg"
				},
				"13_107596213": {
					"id": "13_107596213",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107596213.jpg"
				},
				"15_107595955": {
					"id": "15_107595955",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107595955.jpg"
				},
				"1_107595961": {
					"id": "1_107595961",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107595961.jpg"
				},
				"5_107596205": {
					"id": "5_107596205",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107596205.jpg"
				}
			},
			"name": "BP. Be Proud by BP. Gender Inclusive Bike Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "35.00",
					"maxItemPrice": "35.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "21.00",
					"maxItemPrice": "21.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bp-be-proud-by-bp-gender-inclusive-bike-shorts/5628373",
			"reviewCount": 11,
			"reviewStarRating": 3.6,
			"storeAvailability": null
		},
		"5630172": {
			"id": 5630172,
			"brandId": 7437,
			"brandName": "CANADA GOOSE",
			"styleNumber": "5894619_1",
			"colorCount": 1,
			"colorDefaultId": "classic camo/ rust",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_105969127",
			"colorsById": {
				"classic camo/ rust": {
					"id": "classic camo/ rust",
					"label": "CLASSIC CAMO/ RUST",
					"spriteIndex": 0,
					"mediaIds": [
						"7_105969127",
						"9_105969129",
						"0_105969140"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_105969127"
				}
			},
			"colorIds": [
				"classic camo/ rust"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_105969140": {
					"id": "0_105969140",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_105969140.jpg"
				},
				"7_105969127": {
					"id": "7_105969127",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105969127.jpg"
				},
				"9_105969129": {
					"id": "9_105969129",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_105969129.jpg"
				}
			},
			"name": "Canada Goose Freestyle Trim Fit Down Vest",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "495.00",
					"maxItemPrice": "495.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 25,
					"maxItemPercentOff": 25,
					"minItemPrice": "371.25",
					"maxItemPrice": "371.25",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/canada-goose-freestyle-trim-fit-down-vest/5630172",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5637708": {
			"id": 5637708,
			"brandId": 12656,
			"brandName": "ALLSAINTS",
			"styleNumber": "5643023_4",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_106669610",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"10_106669610",
						"15_106669615"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_106669610"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106669610": {
					"id": "10_106669610",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106669610.jpg"
				},
				"15_106669615": {
					"id": "15_106669615",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106669615.jpg"
				}
			},
			"name": "ALLSAINTS KINO Leather Bomber Jacket",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "498.00",
					"maxItemPrice": "498.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "199.98",
					"maxItemPrice": "199.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/allsaints-kino-leather-bomber-jacket/5637708",
			"reviewCount": 3,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5639652": {
			"id": 5639652,
			"brandId": 998,
			"brandName": "FENDI",
			"styleNumber": "6073067",
			"colorCount": 1,
			"colorDefaultId": "tobacco+yellow",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_107638649",
			"colorsById": {
				"tobacco+yellow": {
					"id": "tobacco+yellow",
					"label": "TOBACCO+YELLOW",
					"spriteIndex": 0,
					"mediaIds": [
						"9_107638649",
						"7_107638667",
						"4_107638664"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "9_107638649"
				}
			},
			"colorIds": [
				"tobacco+yellow"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"4_107638664": {
					"id": "4_107638664",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107638664.jpg"
				},
				"7_107638667": {
					"id": "7_107638667",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107638667.jpg"
				},
				"9_107638649": {
					"id": "9_107638649",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107638649.jpg"
				}
			},
			"name": "Fendi FF Crewneck Sweater",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "890.00",
					"maxItemPrice": "890.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/fendi-ff-crewneck-sweater/5639652",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5644514": {
			"id": 5644514,
			"brandId": 17737,
			"brandName": "OFF-WHITE",
			"styleNumber": "6074514",
			"colorCount": 2,
			"colorDefaultId": "orange black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_107796099-14_107795974",
			"colorsById": {
				"dark green black": {
					"id": "dark green black",
					"label": "DARK GREEN BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_107795974",
						"0_107795980",
						"15_107795975"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "14_107795974"
				},
				"orange black": {
					"id": "orange black",
					"label": "ORANGE BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"19_107796099",
						"4_107796104",
						"1_107796101"
					],
					"standardColors": [
						"Orange"
					],
					"swatchMediaId": "19_107796099"
				}
			},
			"colorIds": [
				"orange black",
				"dark green black"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107795980": {
					"id": "0_107795980",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107795980.jpg"
				},
				"14_107795974": {
					"id": "14_107795974",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107795974.jpg"
				},
				"15_107795975": {
					"id": "15_107795975",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_107795975.jpg"
				},
				"19_107796099": {
					"id": "19_107796099",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107796099.jpg"
				},
				"1_107796101": {
					"id": "1_107796101",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_107796101.jpg"
				},
				"4_107796104": {
					"id": "4_107796104",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107796104.jpg"
				}
			},
			"name": "Off-White Arrows Tie Dye Socks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "110.00",
					"maxItemPrice": "110.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/off-white-arrows-tie-dye-socks/5644514",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5644558": {
			"id": 5644558,
			"brandId": 17737,
			"brandName": "OFF-WHITE",
			"styleNumber": "6074770",
			"colorCount": 1,
			"colorDefaultId": "white black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=17_107854477",
			"colorsById": {
				"white black": {
					"id": "white black",
					"label": "WHITE BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"17_107854477",
						"11_107853291",
						"5_107853285"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "17_107854477"
				}
			},
			"colorIds": [
				"white black"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107853291": {
					"id": "11_107853291",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107853291.jpg"
				},
				"17_107854477": {
					"id": "17_107854477",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107854477.jpg"
				},
				"5_107853285": {
					"id": "5_107853285",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107853285.jpg"
				}
			},
			"name": "Off-White Caravaggio Painting Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "345.00",
					"maxItemPrice": "345.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/off-white-caravaggio-painting-graphic-tee/5644558",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5644560": {
			"id": 5644560,
			"brandId": 17737,
			"brandName": "OFF-WHITE",
			"styleNumber": "6074759",
			"colorCount": 1,
			"colorDefaultId": "black white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_107886433",
			"colorsById": {
				"black white": {
					"id": "black white",
					"label": "BLACK WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_107886433",
						"12_107886232",
						"10_107886230"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_107886433"
				}
			},
			"colorIds": [
				"black white"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107886230": {
					"id": "10_107886230",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107886230.jpg"
				},
				"12_107886232": {
					"id": "12_107886232",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107886232.jpg"
				},
				"13_107886433": {
					"id": "13_107886433",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107886433.jpg"
				}
			},
			"name": "Off-White Logo Cotton Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "275.00",
					"maxItemPrice": "275.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/off-white-logo-cotton-graphic-tee/5644560",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5644573": {
			"id": 5644573,
			"brandId": 17737,
			"brandName": "OFF-WHITE",
			"styleNumber": "6074792",
			"colorCount": 1,
			"colorDefaultId": "dirty medium",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107851940",
			"colorsById": {
				"dirty medium": {
					"id": "dirty medium",
					"label": "DIRTY MEDIUM",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107851940",
						"12_107853252",
						"12_107853232"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_107851940"
				}
			},
			"colorIds": [
				"dirty medium"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107851940": {
					"id": "0_107851940",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107851940.jpg"
				},
				"12_107853232": {
					"id": "12_107853232",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107853232.jpg"
				},
				"12_107853252": {
					"id": "12_107853252",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107853252.jpg"
				}
			},
			"name": "Off-White Logo Distressed Slim Fit Jeans (Dirty Medium)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "975.00",
					"maxItemPrice": "975.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/off-white-logo-distressed-slim-fit-jeans-dirty-medium/5644573",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5647788": {
			"id": 5647788,
			"brandId": 998,
			"brandName": "FENDI",
			"styleNumber": "5945178",
			"colorCount": 1,
			"colorDefaultId": "nero",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_107548770",
			"colorsById": {
				"nero": {
					"id": "nero",
					"label": "NERO",
					"spriteIndex": 0,
					"mediaIds": [
						"10_107548770",
						"13_107548773",
						"12_107548772"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "10_107548770"
				}
			},
			"colorIds": [
				"nero"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107548770": {
					"id": "10_107548770",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107548770.jpg"
				},
				"12_107548772": {
					"id": "12_107548772",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107548772.jpg"
				},
				"13_107548773": {
					"id": "13_107548773",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107548773.jpg"
				}
			},
			"name": "Fendi FF Motif Hooded Sweatshirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "1,290.00",
					"maxItemPrice": "1,290.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/fendi-ff-motif-hooded-sweatshirt/5647788",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5649560": {
			"id": 5649560,
			"brandId": 12792,
			"brandName": "GOOD MAN BRAND",
			"styleNumber": "5906792_7",
			"colorCount": 2,
			"colorDefaultId": "navy clover mid century",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_107478347-19_107192159",
			"colorsById": {
				"blue topaz organic micro dot": {
					"id": "blue topaz organic micro dot",
					"label": "BLUE TOPAZ ORGANIC MICRO DOT",
					"spriteIndex": 1,
					"mediaIds": [
						"19_107192159",
						"5_107192165",
						"3_107192163"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_107192159"
				},
				"navy clover mid century": {
					"id": "navy clover mid century",
					"label": "NAVY CLOVER MID CENTURY",
					"spriteIndex": 0,
					"mediaIds": [
						"7_107478347",
						"11_107478571",
						"3_107478463"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_107478347"
				}
			},
			"colorIds": [
				"navy clover mid century",
				"blue topaz organic micro dot"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107478571": {
					"id": "11_107478571",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107478571.jpg"
				},
				"19_107192159": {
					"id": "19_107192159",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107192159.jpg"
				},
				"3_107192163": {
					"id": "3_107192163",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107192163.jpg"
				},
				"3_107478463": {
					"id": "3_107478463",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107478463.jpg"
				},
				"5_107192165": {
					"id": "5_107192165",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107192165.jpg"
				},
				"7_107478347": {
					"id": "7_107478347",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107478347.jpg"
				}
			},
			"name": "Good Man Brand On Point Slim Fit Button-Up Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "198.00",
					"maxItemPrice": "198.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "78.98",
					"maxItemPrice": "78.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/good-man-brand-on-point-slim-fit-button-up-shirt/5649560",
			"reviewCount": 4,
			"reviewStarRating": 4.5,
			"storeAvailability": null
		},
		"5657639": {
			"id": 5657639,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5940212_2",
			"colorCount": 1,
			"colorDefaultId": "blue estate white waves",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107037618",
			"colorsById": {
				"blue estate white waves": {
					"id": "blue estate white waves",
					"label": "BLUE ESTATE WHITE WAVES",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107037618",
						"18_107038118",
						"0_107037640"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_107037618"
				}
			},
			"colorIds": [
				"blue estate white waves"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107037640": {
					"id": "0_107037640",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107037640.jpg"
				},
				"18_107037618": {
					"id": "18_107037618",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107037618.jpg"
				},
				"18_107038118": {
					"id": "18_107038118",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107038118.jpg"
				}
			},
			"name": "1901 Swim Trunks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "49.50",
					"maxItemPrice": "49.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "19.80",
					"maxItemPrice": "19.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-swim-trunks/5657639",
			"reviewCount": 7,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5658448": {
			"id": 5658448,
			"brandId": 7211,
			"brandName": "CARDINAL OF CANADA",
			"styleNumber": "6078194",
			"colorCount": 1,
			"colorDefaultId": "charcoal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_107790609",
			"colorsById": {
				"charcoal": {
					"id": "charcoal",
					"label": "CHARCOAL",
					"spriteIndex": 0,
					"mediaIds": [
						"9_107790609",
						"13_107790613",
						"11_107790611"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "9_107790609"
				}
			},
			"colorIds": [
				"charcoal"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107790611": {
					"id": "11_107790611",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107790611.jpg"
				},
				"13_107790613": {
					"id": "13_107790613",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107790613.jpg"
				},
				"9_107790609": {
					"id": "9_107790609",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107790609.jpg"
				}
			},
			"name": "Cardinal of Canada Velvet Collar Topcoat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "395.00",
					"maxItemPrice": "395.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 55,
					"maxItemPercentOff": 55,
					"minItemPrice": "177.75",
					"maxItemPrice": "177.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cardinal-of-canada-velvet-collar-topcoat/5658448",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5659145": {
			"id": 5659145,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5722024_2",
			"colorCount": 3,
			"colorDefaultId": "blue estate white gingham",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107343960-14_105006414-2_107307622",
			"colorsById": {
				"blue estate white gingham": {
					"id": "blue estate white gingham",
					"label": "BLUE ESTATE WHITE GINGHAM",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107343960",
						"3_107340863",
						"7_107340847"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_107343960"
				},
				"blue thread gingham": {
					"id": "blue thread gingham",
					"label": "BLUE THREAD GINGHAM",
					"spriteIndex": 1,
					"mediaIds": [
						"14_105006414",
						"3_107649843",
						"7_107340847"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_105006414"
				},
				"red saucy blue gingham": {
					"id": "red saucy blue gingham",
					"label": "RED SAUCY BLUE GINGHAM",
					"spriteIndex": 2,
					"mediaIds": [
						"2_107307622",
						"19_107307639",
						"12_107307632"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "2_107307622"
				}
			},
			"colorIds": [
				"blue estate white gingham",
				"blue thread gingham",
				"red saucy blue gingham"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107343960": {
					"id": "0_107343960",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107343960.jpg"
				},
				"12_107307632": {
					"id": "12_107307632",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107307632.jpg"
				},
				"14_105006414": {
					"id": "14_105006414",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105006414.jpg"
				},
				"19_107307639": {
					"id": "19_107307639",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107307639.jpg"
				},
				"2_107307622": {
					"id": "2_107307622",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107307622.jpg"
				},
				"3_107340863": {
					"id": "3_107340863",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107340863.jpg"
				},
				"3_107649843": {
					"id": "3_107649843",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107649843.jpg"
				},
				"7_107340847": {
					"id": "7_107340847",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107340847.jpg"
				}
			},
			"name": "1901 Heather Gingham Linen Blend Slim Fit Sport Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "69.50",
					"maxItemPrice": "69.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "27.80",
					"maxItemPrice": "27.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-heather-gingham-linen-blend-slim-fit-sport-shirt/5659145",
			"reviewCount": 6,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5659523": {
			"id": 5659523,
			"brandId": 6417,
			"brandName": "1901",
			"styleNumber": "5917782_2",
			"colorCount": 1,
			"colorDefaultId": "grey silk linen madras check",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=11_107166871",
			"colorsById": {
				"grey silk linen madras check": {
					"id": "grey silk linen madras check",
					"label": "GREY SILK LINEN MADRAS CHECK",
					"spriteIndex": 0,
					"mediaIds": [
						"11_107166871",
						"18_107174358",
						"11_107174351"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "11_107166871"
				}
			},
			"colorIds": [
				"grey silk linen madras check"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_107166871": {
					"id": "11_107166871",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107166871.jpg"
				},
				"11_107174351": {
					"id": "11_107174351",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107174351.jpg"
				},
				"18_107174358": {
					"id": "18_107174358",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107174358.jpg"
				}
			},
			"name": "1901 Slim Fit Plaid Button-Down Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "69.50",
					"maxItemPrice": "69.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "27.80",
					"maxItemPrice": "27.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/1901-slim-fit-plaid-button-down-shirt/5659523",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5659925": {
			"id": 5659925,
			"brandId": 5155,
			"brandName": "ETON",
			"styleNumber": "5957377_1",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_106729126",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"6_106729126",
						"16_106733536",
						"4_106729124"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_106729126"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_106733536": {
					"id": "16_106733536",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106733536.jpg"
				},
				"4_106729124": {
					"id": "4_106729124",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106729124.jpg"
				},
				"6_106729126": {
					"id": "6_106729126",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106729126.jpg"
				}
			},
			"name": "Eton Soft Casual Line Slim Fit Jersey Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "225.00",
					"maxItemPrice": "225.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 60,
					"maxItemPercentOff": 60,
					"minItemPrice": "89.98",
					"maxItemPrice": "89.98",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/eton-soft-casual-line-slim-fit-jersey-shirt/5659925",
			"reviewCount": 2,
			"reviewStarRating": 3,
			"storeAvailability": null
		},
		"5667428": {
			"id": 5667428,
			"brandId": 998,
			"brandName": "FENDI",
			"styleNumber": "6073005",
			"colorCount": 1,
			"colorDefaultId": "bianco",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_107634726",
			"colorsById": {
				"bianco": {
					"id": "bianco",
					"label": "BIANCO",
					"spriteIndex": 0,
					"mediaIds": [
						"6_107634726",
						"10_107634730",
						"9_107634729"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "6_107634726"
				}
			},
			"colorIds": [
				"bianco"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107634730": {
					"id": "10_107634730",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107634730.jpg"
				},
				"6_107634726": {
					"id": "6_107634726",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107634726.jpg"
				},
				"9_107634729": {
					"id": "9_107634729",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107634729.jpg"
				}
			},
			"name": "Fendi FF Logo Collar Cotton Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "630.00",
					"maxItemPrice": "630.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/fendi-ff-logo-collar-cotton-shirt/5667428",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5671593": {
			"id": 5671593,
			"brandId": 1515,
			"brandName": "TED BAKER LONDON",
			"styleNumber": "5883295_3",
			"colorCount": 1,
			"colorDefaultId": "coral",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107487232",
			"colorsById": {
				"coral": {
					"id": "coral",
					"label": "CORAL",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107487232",
						"10_107487510",
						"9_107487509"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "12_107487232"
				}
			},
			"colorIds": [
				"coral"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107487510": {
					"id": "10_107487510",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107487510.jpg"
				},
				"12_107487232": {
					"id": "12_107487232",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107487232.jpg"
				},
				"9_107487509": {
					"id": "9_107487509",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107487509.jpg"
				}
			},
			"name": "Ted Baker London Tortila Slim Fit Tipped Pocket Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "99.00",
					"maxItemPrice": "99.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "49.50",
					"maxItemPrice": "49.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ted-baker-london-tortila-slim-fit-tipped-pocket-polo/5671593",
			"reviewCount": 23,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5671679": {
			"id": 5671679,
			"brandId": 6557,
			"brandName": "PETER MILLAR",
			"styleNumber": "5736513_1",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_105991187",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"7_105991187",
						"1_106004721",
						"9_106004709"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_105991187"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"1_106004721": {
					"id": "1_106004721",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106004721.jpg"
				},
				"7_105991187": {
					"id": "7_105991187",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105991187.jpg"
				},
				"9_106004709": {
					"id": "9_106004709",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106004709.jpg"
				}
			},
			"name": "Peter Millar Soft Touch Twill Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "49.00",
					"maxItemPrice": "49.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/peter-millar-soft-touch-twill-shorts/5671679",
			"reviewCount": 4,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5673050": {
			"id": 5673050,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "676951_9",
			"colorCount": 1,
			"colorDefaultId": "robinson",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=2_101972342",
			"colorsById": {
				"robinson": {
					"id": "robinson",
					"label": "ROBINSON",
					"spriteIndex": 0,
					"mediaIds": [
						"2_101972342",
						"15_105991735"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "2_101972342"
				}
			},
			"colorIds": [
				"robinson"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"15_105991735": {
					"id": "15_105991735",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_105991735.jpg"
				},
				"2_101972342": {
					"id": "2_101972342",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_101972342.jpg"
				}
			},
			"name": "AG Graduate Slim Straight Leg Jeans (Robinson)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "188.00",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "132.30",
					"maxItemPrice": "132.30",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-graduate-slim-straight-leg-jeans-robinson/5673050",
			"reviewCount": 123,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5673840": {
			"id": 5673840,
			"brandId": 18070,
			"brandName": "COMME DES GARCONS PLAY",
			"styleNumber": "6082502",
			"colorCount": 1,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=16_107726316",
			"colorsById": {
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"16_107726316",
						"10_107725770",
						"8_107725768"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_107726316"
				}
			},
			"colorIds": [
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107725770": {
					"id": "10_107725770",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107725770.jpg"
				},
				"16_107726316": {
					"id": "16_107726316",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107726316.jpg"
				},
				"8_107725768": {
					"id": "8_107725768",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107725768.jpg"
				}
			},
			"name": "Comme des Garçons PLAY Stripe Long Sleeve Cotton T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "134.00",
					"maxItemPrice": "134.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/comme-des-garcons-play-stripe-long-sleeve-cotton-t-shirt/5673840",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5676281": {
			"id": 5676281,
			"brandId": 748,
			"brandName": "TOMMY BAHAMA",
			"styleNumber": "5970956_2",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_107344189",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"9_107344189",
						"19_107351419",
						"3_107349863"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "9_107344189"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"19_107351419": {
					"id": "19_107351419",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107351419.jpg"
				},
				"3_107349863": {
					"id": "3_107349863",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107349863.jpg"
				},
				"9_107344189": {
					"id": "9_107344189",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107344189.jpg"
				}
			},
			"name": "Tommy Bahama Costa Capri Classic Fit Short Sleeve Linen Blend Button-Up Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "115.00",
					"maxItemPrice": "115.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "69.00",
					"maxItemPrice": "69.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/tommy-bahama-costa-capri-classic-fit-short-sleeve-linen-blend-button-up-shirt/5676281",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5684137": {
			"id": 5684137,
			"brandId": 8111,
			"brandName": "BONOBOS",
			"styleNumber": "5647316_3",
			"colorCount": 11,
			"colorDefaultId": "friday khaki beige/white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_107564059-10_105241830-17_105707077-13_105248873-6_105249066-11_105383411-11_105248851-9_104953249-16_106000896-8_104952928-12_105248952",
			"colorsById": {
				"blue/grey yarn dye": {
					"id": "blue/grey yarn dye",
					"label": "BLUE/GREY YARN DYE",
					"spriteIndex": 1,
					"mediaIds": [
						"10_105241830",
						"15_104953235"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "10_105241830"
				},
				"charcoal herringbone yarn dye": {
					"id": "charcoal herringbone yarn dye",
					"label": "CHARCOAL HERRINGBONE YARN DYE",
					"spriteIndex": 2,
					"mediaIds": [
						"17_105707077",
						"14_105725254"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "17_105707077"
				},
				"coal grey": {
					"id": "coal grey",
					"label": "COAL GREY",
					"spriteIndex": 3,
					"mediaIds": [
						"13_105248873",
						"4_105248764"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "13_105248873"
				},
				"friday grey pattern yarn dye": {
					"id": "friday grey pattern yarn dye",
					"label": "FRIDAY GREY PATTERN YARN DYE",
					"spriteIndex": 4,
					"mediaIds": [
						"6_105249066",
						"7_105249067"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "6_105249066"
				},
				"friday grey yarn dye": {
					"id": "friday grey yarn dye",
					"label": "FRIDAY GREY YARN DYE",
					"spriteIndex": 5,
					"mediaIds": [
						"11_105383411",
						"8_104950028"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "11_105383411"
				},
				"friday khaki beige/white": {
					"id": "friday khaki beige/white",
					"label": "FRIDAY KHAKI BEIGE/WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"19_107564059",
						"12_107564052"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "19_107564059"
				},
				"friday steel": {
					"id": "friday steel",
					"label": "FRIDAY STEEL",
					"spriteIndex": 6,
					"mediaIds": [
						"11_105248851",
						"4_104556084"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "11_105248851"
				},
				"light khaki yarn dye": {
					"id": "light khaki yarn dye",
					"label": "LIGHT KHAKI YARN DYE",
					"spriteIndex": 7,
					"mediaIds": [
						"9_104953249",
						"14_104953254"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "9_104953249"
				},
				"monday blues": {
					"id": "monday blues",
					"label": "MONDAY BLUES",
					"spriteIndex": 8,
					"mediaIds": [
						"16_106000896",
						"19_106000899"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "16_106000896"
				},
				"tuesday charcoal yarn dye": {
					"id": "tuesday charcoal yarn dye",
					"label": "TUESDAY CHARCOAL YARN DYE",
					"spriteIndex": 9,
					"mediaIds": [
						"8_104952928",
						"2_104952942"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "8_104952928"
				},
				"wednesday wheat": {
					"id": "wednesday wheat",
					"label": "WEDNESDAY WHEAT",
					"spriteIndex": 10,
					"mediaIds": [
						"12_105248952",
						"12_104624092"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "12_105248952"
				}
			},
			"colorIds": [
				"friday khaki beige/white",
				"blue/grey yarn dye",
				"charcoal herringbone yarn dye",
				"coal grey",
				"friday grey pattern yarn dye",
				"friday grey yarn dye",
				"friday steel",
				"light khaki yarn dye",
				"monday blues",
				"tuesday charcoal yarn dye",
				"wednesday wheat"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_105241830": {
					"id": "10_105241830",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_105241830.jpg"
				},
				"11_105248851": {
					"id": "11_105248851",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105248851.jpg"
				},
				"11_105383411": {
					"id": "11_105383411",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_105383411.jpg"
				},
				"12_104624092": {
					"id": "12_104624092",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_104624092.jpg"
				},
				"12_105248952": {
					"id": "12_105248952",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_105248952.jpg"
				},
				"12_107564052": {
					"id": "12_107564052",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107564052.jpg"
				},
				"13_105248873": {
					"id": "13_105248873",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_105248873.jpg"
				},
				"14_104953254": {
					"id": "14_104953254",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_104953254.jpg"
				},
				"14_105725254": {
					"id": "14_105725254",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_105725254.jpg"
				},
				"15_104953235": {
					"id": "15_104953235",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_104953235.jpg"
				},
				"16_106000896": {
					"id": "16_106000896",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106000896.jpg"
				},
				"17_105707077": {
					"id": "17_105707077",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_105707077.jpg"
				},
				"19_106000899": {
					"id": "19_106000899",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106000899.jpg"
				},
				"19_107564059": {
					"id": "19_107564059",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107564059.jpg"
				},
				"2_104952942": {
					"id": "2_104952942",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_104952942.jpg"
				},
				"4_104556084": {
					"id": "4_104556084",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_104556084.jpg"
				},
				"4_105248764": {
					"id": "4_105248764",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_105248764.jpg"
				},
				"6_105249066": {
					"id": "6_105249066",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_105249066.jpg"
				},
				"7_105249067": {
					"id": "7_105249067",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_105249067.jpg"
				},
				"8_104950028": {
					"id": "8_104950028",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_104950028.jpg"
				},
				"8_104952928": {
					"id": "8_104952928",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_104952928.jpg"
				},
				"9_104953249": {
					"id": "9_104953249",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_104953249.jpg"
				}
			},
			"name": "Bonobos Stretch Weekday Warrior Slim Fit Dress Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bonobos-stretch-weekday-warrior-slim-fit-dress-pants/5684137",
			"reviewCount": 64,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5686798": {
			"id": 5686798,
			"brandId": 19344,
			"brandName": "PALM ANGELS",
			"styleNumber": "6088524",
			"colorCount": 1,
			"colorDefaultId": "aquamarine w",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_107811867",
			"colorsById": {
				"aquamarine w": {
					"id": "aquamarine w",
					"label": "AQUAMARINE W",
					"spriteIndex": 0,
					"mediaIds": [
						"7_107811867",
						"17_107811877",
						"16_107811876"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_107811867"
				}
			},
			"colorIds": [
				"aquamarine w"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_107811876": {
					"id": "16_107811876",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107811876.jpg"
				},
				"17_107811877": {
					"id": "17_107811877",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_107811877.jpg"
				},
				"7_107811867": {
					"id": "7_107811867",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107811867.jpg"
				}
			},
			"name": "Palm Angels Ice Bear Cotton Hoodie",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "770.00",
					"maxItemPrice": "770.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/palm-angels-ice-bear-cotton-hoodie/5686798",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5686802": {
			"id": 5686802,
			"brandId": 19344,
			"brandName": "PALM ANGELS",
			"styleNumber": "6088530",
			"colorCount": 2,
			"colorDefaultId": "purple metal",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_107811847-9_107710429",
			"colorsById": {
				"purple metal": {
					"id": "purple metal",
					"label": "PURPLE METAL",
					"spriteIndex": 0,
					"mediaIds": [
						"7_107811847",
						"2_107811882",
						"19_107811879"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "7_107811847"
				},
				"white metal": {
					"id": "white metal",
					"label": "WHITE METAL",
					"spriteIndex": 1,
					"mediaIds": [
						"9_107710429",
						"6_107710446",
						"4_107710444"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "9_107710429"
				}
			},
			"colorIds": [
				"purple metal",
				"white metal"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"19_107811879": {
					"id": "19_107811879",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107811879.jpg"
				},
				"2_107811882": {
					"id": "2_107811882",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107811882.jpg"
				},
				"4_107710444": {
					"id": "4_107710444",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107710444.jpg"
				},
				"6_107710446": {
					"id": "6_107710446",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107710446.jpg"
				},
				"7_107811847": {
					"id": "7_107811847",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_107811847.jpg"
				},
				"9_107710429": {
					"id": "9_107710429",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107710429.jpg"
				}
			},
			"name": "Palm Angels Blank Logo Graphic Tee",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "300.00",
					"maxItemPrice": "300.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/palm-angels-blank-logo-graphic-tee/5686802",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5687819": {
			"id": 5687819,
			"brandId": 17332,
			"brandName": "MATOUK",
			"styleNumber": "6088695",
			"colorCount": 3,
			"colorDefaultId": "pool",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_107663186-0_107663180-3_107663183",
			"colorsById": {
				"anthracite": {
					"id": "anthracite",
					"label": "ANTHRACITE",
					"spriteIndex": 1,
					"mediaIds": [
						"0_107663180",
						"2_107663182",
						"5_107666505"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "0_107663180"
				},
				"pool": {
					"id": "pool",
					"label": "POOL",
					"spriteIndex": 0,
					"mediaIds": [
						"6_107663186",
						"11_107663191",
						"5_107666505"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_107663186"
				},
				"silver": {
					"id": "silver",
					"label": "SILVER",
					"spriteIndex": 2,
					"mediaIds": [
						"3_107663183",
						"5_107663185",
						"5_107666505"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_107663183"
				}
			},
			"colorIds": [
				"pool",
				"anthracite",
				"silver"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107663180": {
					"id": "0_107663180",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107663180.jpg"
				},
				"11_107663191": {
					"id": "11_107663191",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107663191.jpg"
				},
				"2_107663182": {
					"id": "2_107663182",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_107663182.jpg"
				},
				"3_107663183": {
					"id": "3_107663183",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107663183.jpg"
				},
				"5_107663185": {
					"id": "5_107663185",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107663185.jpg"
				},
				"5_107666505": {
					"id": "5_107666505",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107666505.jpg"
				},
				"6_107663186": {
					"id": "6_107663186",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107663186.jpg"
				}
			},
			"name": "Matouk Kiran Robe",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "99.00",
					"maxItemPrice": "99.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/matouk-kiran-robe/5687819",
			"reviewCount": 3,
			"reviewStarRating": 4.3,
			"storeAvailability": null
		},
		"5688137": {
			"id": 5688137,
			"brandId": 8416,
			"brandName": "LIVERPOOL",
			"styleNumber": "6089000",
			"colorCount": 4,
			"colorDefaultId": "khaki",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=4_107758464-13_107758453-19_107758459-6_107758466",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"13_107758453",
						"5_107732085"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "13_107758453"
				},
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"19_107758459",
						"14_107732094"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_107758459"
				},
				"khaki": {
					"id": "khaki",
					"label": "KHAKI",
					"spriteIndex": 0,
					"mediaIds": [
						"4_107758464",
						"0_107747040"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "4_107758464"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 3,
					"mediaIds": [
						"6_107758466",
						"5_107732105"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "6_107758466"
				}
			},
			"colorIds": [
				"khaki",
				"black",
				"grey",
				"navy"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107747040": {
					"id": "0_107747040",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107747040.jpg"
				},
				"13_107758453": {
					"id": "13_107758453",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107758453.jpg"
				},
				"14_107732094": {
					"id": "14_107732094",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107732094.jpg"
				},
				"19_107758459": {
					"id": "19_107758459",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107758459.jpg"
				},
				"4_107758464": {
					"id": "4_107758464",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107758464.jpg"
				},
				"5_107732085": {
					"id": "5_107732085",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107732085.jpg"
				},
				"5_107732105": {
					"id": "5_107732105",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107732105.jpg"
				},
				"6_107758466": {
					"id": "6_107758466",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_107758466.jpg"
				}
			},
			"name": "Liverpool Shawl Collar Cardigan",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "98.00",
					"maxItemPrice": "98.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/liverpool-shawl-collar-cardigan/5688137",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5688457": {
			"id": 5688457,
			"brandId": 4317,
			"brandName": "ROBERT BARAKETT",
			"styleNumber": "36349_5",
			"colorCount": 6,
			"colorDefaultId": "purple haze",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_106500972-2_106369002-3_106303823-0_107182580-7_106777527-14_106945894",
			"colorsById": {
				"griffin grey": {
					"id": "griffin grey",
					"label": "GRIFFIN GREY",
					"spriteIndex": 1,
					"mediaIds": [
						"2_106369002",
						"4_106369004",
						"5_106369225"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "2_106369002"
				},
				"live blue": {
					"id": "live blue",
					"label": "LIVE BLUE",
					"spriteIndex": 2,
					"mediaIds": [
						"3_106303823",
						"15_106303835",
						"14_106303834"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "3_106303823"
				},
				"pale yellow": {
					"id": "pale yellow",
					"label": "PALE YELLOW",
					"spriteIndex": 3,
					"mediaIds": [
						"0_107182580",
						"3_107182823",
						"4_107182724"
					],
					"standardColors": [
						"Yellow"
					],
					"swatchMediaId": "0_107182580"
				},
				"purple haze": {
					"id": "purple haze",
					"label": "PURPLE HAZE",
					"spriteIndex": 0,
					"mediaIds": [
						"12_106500972",
						"12_106723572",
						"13_106723573"
					],
					"standardColors": [
						"Purple"
					],
					"swatchMediaId": "12_106500972"
				},
				"shadow green": {
					"id": "shadow green",
					"label": "SHADOW GREEN",
					"spriteIndex": 4,
					"mediaIds": [
						"7_106777527",
						"10_106777590",
						"13_106777593"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "7_106777527"
				},
				"woodrose": {
					"id": "woodrose",
					"label": "WOODROSE",
					"spriteIndex": 5,
					"mediaIds": [
						"14_106945894",
						"4_106945904",
						"1_106945901"
					],
					"standardColors": [
						"Pink"
					],
					"swatchMediaId": "14_106945894"
				}
			},
			"colorIds": [
				"purple haze",
				"griffin grey",
				"live blue",
				"pale yellow",
				"shadow green",
				"woodrose"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107182580": {
					"id": "0_107182580",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107182580.jpg"
				},
				"10_106777590": {
					"id": "10_106777590",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106777590.jpg"
				},
				"12_106500972": {
					"id": "12_106500972",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106500972.jpg"
				},
				"12_106723572": {
					"id": "12_106723572",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_106723572.jpg"
				},
				"13_106723573": {
					"id": "13_106723573",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106723573.jpg"
				},
				"13_106777593": {
					"id": "13_106777593",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106777593.jpg"
				},
				"14_106303834": {
					"id": "14_106303834",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106303834.jpg"
				},
				"14_106945894": {
					"id": "14_106945894",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106945894.jpg"
				},
				"15_106303835": {
					"id": "15_106303835",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_106303835.jpg"
				},
				"1_106945901": {
					"id": "1_106945901",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106945901.jpg"
				},
				"2_106369002": {
					"id": "2_106369002",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106369002.jpg"
				},
				"3_106303823": {
					"id": "3_106303823",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_106303823.jpg"
				},
				"3_107182823": {
					"id": "3_107182823",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107182823.jpg"
				},
				"4_106369004": {
					"id": "4_106369004",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106369004.jpg"
				},
				"4_106945904": {
					"id": "4_106945904",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_106945904.jpg"
				},
				"4_107182724": {
					"id": "4_107182724",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107182724.jpg"
				},
				"5_106369225": {
					"id": "5_106369225",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106369225.jpg"
				},
				"7_106777527": {
					"id": "7_106777527",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106777527.jpg"
				}
			},
			"name": "Robert Barakett Georgia Crewneck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "59.50",
					"maxItemPrice": "59.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 50,
					"minItemPrice": "29.75",
					"maxItemPrice": "35.70",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/robert-barakett-georgia-crewneck-t-shirt/5688457",
			"reviewCount": 456,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5689291": {
			"id": 5689291,
			"brandId": 17825,
			"brandName": "GREYSON",
			"styleNumber": "5933169_2",
			"colorCount": 3,
			"colorDefaultId": "eel",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=7_106658947-5_106557625-6_106557706",
			"colorsById": {
				"eel": {
					"id": "eel",
					"label": "EEL",
					"spriteIndex": 0,
					"mediaIds": [
						"7_106658947",
						"8_106658968"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "7_106658947"
				},
				"maltese": {
					"id": "maltese",
					"label": "MALTESE",
					"spriteIndex": 1,
					"mediaIds": [
						"5_106557625",
						"14_106565494"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_106557625"
				},
				"shepherd": {
					"id": "shepherd",
					"label": "SHEPHERD",
					"spriteIndex": 2,
					"mediaIds": [
						"6_106557706",
						"8_106565468"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "6_106557706"
				}
			},
			"colorIds": [
				"eel",
				"maltese",
				"shepherd"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_106565494": {
					"id": "14_106565494",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_106565494.jpg"
				},
				"5_106557625": {
					"id": "5_106557625",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106557625.jpg"
				},
				"6_106557706": {
					"id": "6_106557706",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_106557706.jpg"
				},
				"7_106658947": {
					"id": "7_106658947",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_106658947.jpg"
				},
				"8_106565468": {
					"id": "8_106565468",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106565468.jpg"
				},
				"8_106658968": {
					"id": "8_106658968",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_106658968.jpg"
				}
			},
			"name": "Greyson Montauk Slim Straight Stretch Nylon Technical Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "130.00",
					"maxItemPrice": "130.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 50,
					"maxItemPercentOff": 50,
					"minItemPrice": "65.00",
					"maxItemPrice": "65.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/greyson-montauk-slim-straight-stretch-nylon-technical-pants/5689291",
			"reviewCount": 3,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5689626": {
			"id": 5689626,
			"brandId": 7211,
			"brandName": "CARDINAL OF CANADA",
			"styleNumber": "6078193_1",
			"colorCount": 1,
			"colorDefaultId": "camel",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=0_107610160",
			"colorsById": {
				"camel": {
					"id": "camel",
					"label": "CAMEL",
					"spriteIndex": 0,
					"mediaIds": [
						"0_107610160",
						"5_107609945",
						"0_107609940"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "0_107610160"
				}
			},
			"colorIds": [
				"camel"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107609940": {
					"id": "0_107609940",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107609940.jpg"
				},
				"0_107610160": {
					"id": "0_107610160",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107610160.jpg"
				},
				"5_107609945": {
					"id": "5_107609945",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107609945.jpg"
				}
			},
			"name": "Cardinal of Canada Wool Blend Topcoat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "395.00",
					"maxItemPrice": "395.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 55,
					"maxItemPercentOff": 55,
					"minItemPrice": "177.75",
					"maxItemPrice": "177.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cardinal-of-canada-wool-blend-topcoat/5689626",
			"reviewCount": 1,
			"reviewStarRating": 4,
			"storeAvailability": null
		},
		"5693293": {
			"id": 5693293,
			"brandId": 168,
			"brandName": "Cutter & Buck",
			"styleNumber": "5304334_3",
			"colorCount": 9,
			"colorDefaultId": "serene",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=19_106221939-5_100874425-1_100874321-0_106171660-18_100873958-18_100873758-3_100874163-12_100873872-15_100873995",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"5_100874425",
						"16_100874416",
						"12_100873932"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "5_100874425"
				},
				"card red": {
					"id": "card red",
					"label": "CARD RED",
					"spriteIndex": 2,
					"mediaIds": [
						"1_100874321",
						"19_100874319",
						"17_100873837"
					],
					"standardColors": [
						"Red"
					],
					"swatchMediaId": "1_100874321"
				},
				"chambers": {
					"id": "chambers",
					"label": "CHAMBERS",
					"spriteIndex": 3,
					"mediaIds": [
						"0_106171660",
						"16_106165036",
						"17_106170177"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "0_106171660"
				},
				"cilantro": {
					"id": "cilantro",
					"label": "CILANTRO",
					"spriteIndex": 4,
					"mediaIds": [
						"18_100873958",
						"16_100873956",
						"13_100873693"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "18_100873958"
				},
				"digital": {
					"id": "digital",
					"label": "DIGITAL",
					"spriteIndex": 5,
					"mediaIds": [
						"18_100873758",
						"12_100873752",
						"12_100874312"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "18_100873758"
				},
				"elemental": {
					"id": "elemental",
					"label": "ELEMENTAL",
					"spriteIndex": 6,
					"mediaIds": [
						"3_100874163",
						"18_100874158",
						"14_100873714"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "3_100874163"
				},
				"liberty navy": {
					"id": "liberty navy",
					"label": "LIBERTY NAVY",
					"spriteIndex": 7,
					"mediaIds": [
						"12_100873872",
						"3_100873863",
						"6_100873886"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "12_100873872"
				},
				"sea blue": {
					"id": "sea blue",
					"label": "SEA BLUE",
					"spriteIndex": 8,
					"mediaIds": [
						"15_100873995",
						"13_100873993",
						"16_100873736"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "15_100873995"
				},
				"serene": {
					"id": "serene",
					"label": "SERENE",
					"spriteIndex": 0,
					"mediaIds": [
						"19_106221939",
						"2_106221942",
						"1_106221941"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "19_106221939"
				}
			},
			"colorIds": [
				"serene",
				"black",
				"card red",
				"chambers",
				"cilantro",
				"digital",
				"elemental",
				"liberty navy",
				"sea blue"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_106171660": {
					"id": "0_106171660",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_106171660.jpg"
				},
				"12_100873752": {
					"id": "12_100873752",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_100873752.jpg"
				},
				"12_100873872": {
					"id": "12_100873872",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_100873872.jpg"
				},
				"12_100873932": {
					"id": "12_100873932",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_100873932.jpg"
				},
				"12_100874312": {
					"id": "12_100874312",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_100874312.jpg"
				},
				"13_100873693": {
					"id": "13_100873693",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_100873693.jpg"
				},
				"13_100873993": {
					"id": "13_100873993",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_100873993.jpg"
				},
				"14_100873714": {
					"id": "14_100873714",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_100873714.jpg"
				},
				"15_100873995": {
					"id": "15_100873995",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/15/_100873995.jpg"
				},
				"16_100873736": {
					"id": "16_100873736",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100873736.jpg"
				},
				"16_100873956": {
					"id": "16_100873956",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100873956.jpg"
				},
				"16_100874416": {
					"id": "16_100874416",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_100874416.jpg"
				},
				"16_106165036": {
					"id": "16_106165036",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_106165036.jpg"
				},
				"17_100873837": {
					"id": "17_100873837",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_100873837.jpg"
				},
				"17_106170177": {
					"id": "17_106170177",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/17/_106170177.jpg"
				},
				"18_100873758": {
					"id": "18_100873758",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_100873758.jpg"
				},
				"18_100873958": {
					"id": "18_100873958",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_100873958.jpg"
				},
				"18_100874158": {
					"id": "18_100874158",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_100874158.jpg"
				},
				"19_100874319": {
					"id": "19_100874319",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_100874319.jpg"
				},
				"19_106221939": {
					"id": "19_106221939",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_106221939.jpg"
				},
				"1_100874321": {
					"id": "1_100874321",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_100874321.jpg"
				},
				"1_106221941": {
					"id": "1_106221941",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/1/_106221941.jpg"
				},
				"2_106221942": {
					"id": "2_106221942",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106221942.jpg"
				},
				"3_100873863": {
					"id": "3_100873863",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_100873863.jpg"
				},
				"3_100874163": {
					"id": "3_100874163",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_100874163.jpg"
				},
				"5_100874425": {
					"id": "5_100874425",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_100874425.jpg"
				},
				"6_100873886": {
					"id": "6_100873886",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_100873886.jpg"
				}
			},
			"name": "Cutter & Buck Advantage Golf Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "65.00",
					"maxItemPrice": "65.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 50,
					"minItemPrice": "32.50",
					"maxItemPrice": "65.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/cutter-buck-advantage-golf-polo/5693293",
			"reviewCount": 12,
			"reviewStarRating": 4.9,
			"storeAvailability": null
		},
		"5693860": {
			"id": 5693860,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5359890_17",
			"colorCount": 3,
			"colorDefaultId": "portobello road",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=9_107773449-11_103433431-19_103585239",
			"colorsById": {
				"blue vault": {
					"id": "blue vault",
					"label": "BLUE VAULT",
					"spriteIndex": 1,
					"mediaIds": [
						"11_103433431",
						"18_103433438",
						"18_103432818"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "11_103433431"
				},
				"dark rock": {
					"id": "dark rock",
					"label": "DARK ROCK",
					"spriteIndex": 2,
					"mediaIds": [
						"19_103585239",
						"4_103585244",
						"16_103583036"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_103585239"
				},
				"portobello road": {
					"id": "portobello road",
					"label": "PORTOBELLO ROAD",
					"spriteIndex": 0,
					"mediaIds": [
						"9_107773449",
						"12_107771332",
						"11_107771331"
					],
					"standardColors": [
						"Brown"
					],
					"swatchMediaId": "9_107773449"
				}
			},
			"colorIds": [
				"portobello road",
				"blue vault",
				"dark rock"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"11_103433431": {
					"id": "11_103433431",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_103433431.jpg"
				},
				"11_107771331": {
					"id": "11_107771331",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_107771331.jpg"
				},
				"12_107771332": {
					"id": "12_107771332",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107771332.jpg"
				},
				"16_103583036": {
					"id": "16_103583036",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_103583036.jpg"
				},
				"18_103432818": {
					"id": "18_103432818",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103432818.jpg"
				},
				"18_103433438": {
					"id": "18_103433438",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_103433438.jpg"
				},
				"19_103585239": {
					"id": "19_103585239",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_103585239.jpg"
				},
				"4_103585244": {
					"id": "4_103585244",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_103585244.jpg"
				},
				"9_107773449": {
					"id": "9_107773449",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107773449.jpg"
				}
			},
			"name": "AG Everett SUD Slim Straight Fit Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "188.00",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-everett-sud-slim-straight-fit-pants/5693860",
			"reviewCount": 176,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5695673": {
			"id": 5695673,
			"brandId": 5227,
			"brandName": "ZELLA",
			"styleNumber": "5271720_3",
			"colorCount": 1,
			"colorDefaultId": "navy halite melange",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_106730133",
			"colorsById": {
				"navy halite melange": {
					"id": "navy halite melange",
					"label": "NAVY HALITE MELANGE",
					"spriteIndex": 0,
					"mediaIds": [
						"13_106730133",
						"5_106726525",
						"2_106726522"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "13_106730133"
				}
			},
			"colorIds": [
				"navy halite melange"
			],
			"enticementIds": [],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"13_106730133": {
					"id": "13_106730133",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_106730133.jpg"
				},
				"2_106726522": {
					"id": "2_106726522",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106726522.jpg"
				},
				"5_106726525": {
					"id": "5_106726525",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_106726525.jpg"
				}
			},
			"name": "Zella Pyrite Knit Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "49.00",
					"maxItemPrice": "49.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/zella-pyrite-knit-shorts/5695673",
			"reviewCount": 65,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5698785": {
			"id": 5698785,
			"brandId": 18457,
			"brandName": "BOMBAS",
			"styleNumber": "6018083_1",
			"colorCount": 4,
			"colorDefaultId": "navy",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_107358774-18_107358778-19_107358779-12_107358772",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"18_107358778",
						"3_107358763"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "18_107358778"
				},
				"grey": {
					"id": "grey",
					"label": "GREY",
					"spriteIndex": 2,
					"mediaIds": [
						"19_107358779",
						"9_107358769"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "19_107358779"
				},
				"navy": {
					"id": "navy",
					"label": "NAVY",
					"spriteIndex": 0,
					"mediaIds": [
						"14_107358774",
						"16_107358776"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "14_107358774"
				},
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 3,
					"mediaIds": [
						"12_107358772",
						"8_107358248"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "12_107358772"
				}
			},
			"colorIds": [
				"navy",
				"black",
				"grey",
				"white"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107358772": {
					"id": "12_107358772",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107358772.jpg"
				},
				"14_107358774": {
					"id": "14_107358774",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107358774.jpg"
				},
				"16_107358776": {
					"id": "16_107358776",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107358776.jpg"
				},
				"18_107358778": {
					"id": "18_107358778",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107358778.jpg"
				},
				"19_107358779": {
					"id": "19_107358779",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107358779.jpg"
				},
				"3_107358763": {
					"id": "3_107358763",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_107358763.jpg"
				},
				"8_107358248": {
					"id": "8_107358248",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/8/_107358248.jpg"
				},
				"9_107358769": {
					"id": "9_107358769",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_107358769.jpg"
				}
			},
			"name": "Bombas 3-Pack Cushion No-Show Socks",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "33.00",
					"maxItemPrice": "33.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bombas-3-pack-cushion-no-show-socks/5698785",
			"reviewCount": 11,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5701303": {
			"id": 5701303,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5893389_2",
			"colorCount": 3,
			"colorDefaultId": "heather grey",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=12_107216392-14_107216414-5_107216305",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 1,
					"mediaIds": [
						"14_107216414",
						"2_106929702"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "14_107216414"
				},
				"blue bay/ minnow/ medieval": {
					"id": "blue bay/ minnow/ medieval",
					"label": "BLUE BAY/ MINNOW/ MEDIEVAL",
					"spriteIndex": 2,
					"mediaIds": [
						"5_107216305",
						"18_107216298"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "5_107216305"
				},
				"heather grey": {
					"id": "heather grey",
					"label": "HEATHER GREY",
					"spriteIndex": 0,
					"mediaIds": [
						"12_107216392",
						"16_107216396"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "12_107216392"
				}
			},
			"colorIds": [
				"heather grey",
				"black",
				"blue bay/ minnow/ medieval"
			],
			"enticementIds": [
				"priceMatched"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"12_107216392": {
					"id": "12_107216392",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/12/_107216392.jpg"
				},
				"14_107216414": {
					"id": "14_107216414",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107216414.jpg"
				},
				"16_107216396": {
					"id": "16_107216396",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107216396.jpg"
				},
				"18_107216298": {
					"id": "18_107216298",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107216298.jpg"
				},
				"2_106929702": {
					"id": "2_106929702",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/2/_106929702.jpg"
				},
				"5_107216305": {
					"id": "5_107216305",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_107216305.jpg"
				}
			},
			"name": "Calvin Klein 3-Pack Boxer Briefs",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "42.50",
					"maxItemPrice": "42.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 20,
					"maxItemPercentOff": 20,
					"minItemPrice": "34.00",
					"maxItemPrice": "34.00",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-3-pack-boxer-briefs/5701303",
			"reviewCount": 32,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5702413": {
			"id": 5702413,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5681671_2",
			"colorCount": 1,
			"colorDefaultId": "black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_104819426",
			"colorsById": {
				"black": {
					"id": "black",
					"label": "BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"6_104819426",
						"7_104819427"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "6_104819426"
				}
			},
			"colorIds": [
				"black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"6_104819426": {
					"id": "6_104819426",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_104819426.jpg"
				},
				"7_104819427": {
					"id": "7_104819427",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/7/_104819427.jpg"
				}
			},
			"name": "Calvin Klein Ultrasoft Stretch Modal V-Neck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "34.00",
					"maxItemPrice": "34.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "23.80",
					"maxItemPrice": "23.80",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-ultrasoft-stretch-modal-v-neck-t-shirt/5702413",
			"reviewCount": 45,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5702415": {
			"id": 5702415,
			"brandId": 5111,
			"brandName": "CALVIN KLEIN",
			"styleNumber": "5893379_1",
			"colorCount": 1,
			"colorDefaultId": "white",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=14_107215894",
			"colorsById": {
				"white": {
					"id": "white",
					"label": "WHITE",
					"spriteIndex": 0,
					"mediaIds": [
						"14_107215894",
						"19_107215899"
					],
					"standardColors": [
						"White"
					],
					"swatchMediaId": "14_107215894"
				}
			},
			"colorIds": [
				"white"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"14_107215894": {
					"id": "14_107215894",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/14/_107215894.jpg"
				},
				"19_107215899": {
					"id": "19_107215899",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107215899.jpg"
				}
			},
			"name": "Calvin Klein 3-Pack Slim Fit Cotton V-Neck T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "42.50",
					"maxItemPrice": "42.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "29.75",
					"maxItemPrice": "29.75",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/calvin-klein-3-pack-slim-fit-cotton-v-neck-t-shirt/5702415",
			"reviewCount": 28,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		},
		"5715014": {
			"id": 5715014,
			"brandId": 748,
			"brandName": "TOMMY BAHAMA",
			"styleNumber": "5649498_2",
			"colorCount": 1,
			"colorDefaultId": "none",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=",
			"colorsById": {
				"none": {
					"id": "none",
					"label": "",
					"spriteIndex": 0,
					"mediaIds": [
						"16_104941336"
					],
					"standardColors": null,
					"swatchMediaId": ""
				}
			},
			"colorIds": [
				"none"
			],
			"enticementIds": [
				"new"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_104941336": {
					"id": "16_104941336",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_104941336.jpg"
				}
			},
			"name": "Tommy Bahama Emfielder 2.0 IslandZone® Performance Polo",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "89.50",
					"maxItemPrice": "89.50",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 40,
					"minItemPrice": "53.70",
					"maxItemPrice": "89.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/tommy-bahama-emfielder-2-0-islandzone-performance-polo/5715014",
			"reviewCount": 1,
			"reviewStarRating": 5,
			"storeAvailability": null
		},
		"5735775": {
			"id": 5735775,
			"brandId": 5160,
			"brandName": "VINEYARD VINES",
			"styleNumber": "5917199_1",
			"colorCount": 1,
			"colorDefaultId": "grey heather",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_107287650",
			"colorsById": {
				"grey heather": {
					"id": "grey heather",
					"label": "GREY HEATHER",
					"spriteIndex": 0,
					"mediaIds": [
						"10_107287650",
						"10_107305750",
						"4_107287664"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "10_107287650"
				}
			},
			"colorIds": [
				"grey heather"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_107287650": {
					"id": "10_107287650",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107287650.jpg"
				},
				"10_107305750": {
					"id": "10_107305750",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_107305750.jpg"
				},
				"4_107287664": {
					"id": "4_107287664",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/4/_107287664.jpg"
				}
			},
			"name": "vineyard vines Whale Pocket T-Shirt",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "42.00",
					"maxItemPrice": "42.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "25.20",
					"maxItemPrice": "25.20",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/vineyard-vines-whale-pocket-t-shirt/5735775",
			"reviewCount": 5,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5736015": {
			"id": 5736015,
			"brandId": 13230,
			"brandName": "NORDSTROM MENS SHOP",
			"styleNumber": "5986663_1",
			"colorCount": 1,
			"colorDefaultId": "grey chateau",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=18_107576378",
			"colorsById": {
				"grey chateau": {
					"id": "grey chateau",
					"label": "GREY CHATEAU",
					"spriteIndex": 0,
					"mediaIds": [
						"18_107576378",
						"16_107576376"
					],
					"standardColors": [
						"Grey"
					],
					"swatchMediaId": "18_107576378"
				}
			},
			"colorIds": [
				"grey chateau"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": true,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"16_107576376": {
					"id": "16_107576376",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/16/_107576376.jpg"
				},
				"18_107576378": {
					"id": "18_107576378",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_107576378.jpg"
				}
			},
			"name": "Nordstrom Men's Shop Slim Fit Sport Coat",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "149.00",
					"maxItemPrice": "149.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 40,
					"maxItemPercentOff": 40,
					"minItemPrice": "89.40",
					"maxItemPrice": "89.40",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/nordstrom-mens-shop-slim-fit-sport-coat/5736015",
			"reviewCount": 0,
			"reviewStarRating": 0,
			"storeAvailability": null
		},
		"5737862": {
			"id": 5737862,
			"brandId": 8111,
			"brandName": "BONOBOS",
			"styleNumber": "5220991_13",
			"colorCount": 1,
			"colorDefaultId": "nopales",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=13_107033273",
			"colorsById": {
				"nopales": {
					"id": "nopales",
					"label": "NOPALES",
					"spriteIndex": 0,
					"mediaIds": [
						"13_107033273",
						"0_107033200",
						"19_107033199"
					],
					"standardColors": [
						"Green"
					],
					"swatchMediaId": "13_107033273"
				}
			},
			"colorIds": [
				"nopales"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"0_107033200": {
					"id": "0_107033200",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/0/_107033200.jpg"
				},
				"13_107033273": {
					"id": "13_107033273",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/13/_107033273.jpg"
				},
				"19_107033199": {
					"id": "19_107033199",
					"group": "alt",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/19/_107033199.jpg"
				}
			},
			"name": "Bonobos Stretch Washed Chino 7-Inch Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "78.00",
					"maxItemPrice": "78.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 33,
					"maxItemPercentOff": 33,
					"minItemPrice": "52.26",
					"maxItemPrice": "52.26",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/bonobos-stretch-washed-chino-7-inch-shorts/5737862",
			"reviewCount": 39,
			"reviewStarRating": 4.4,
			"storeAvailability": null
		},
		"5743197": {
			"id": 5743197,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "676951_10",
			"colorCount": 1,
			"colorDefaultId": "jack",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=3_101970543",
			"colorsById": {
				"jack": {
					"id": "jack",
					"label": "JACK",
					"spriteIndex": 0,
					"mediaIds": [
						"3_101970543",
						"18_10716598"
					],
					"standardColors": [
						"Blue"
					],
					"swatchMediaId": "3_101970543"
				}
			},
			"colorIds": [
				"jack"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"18_10716598": {
					"id": "18_10716598",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/18/_10716598.jpg"
				},
				"3_101970543": {
					"id": "3_101970543",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/3/_101970543.jpg"
				}
			},
			"name": "AG Graduate Slim Straight Leg Jeans (Robinson)",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "178.00",
					"maxItemPrice": "178.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "124.60",
					"maxItemPrice": "124.60",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-graduate-slim-straight-leg-jeans-robinson/5743197",
			"reviewCount": 123,
			"reviewStarRating": 4.6,
			"storeAvailability": null
		},
		"5743201": {
			"id": 5743201,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5359890_18",
			"colorCount": 1,
			"colorDefaultId": "super black",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=6_100955206",
			"colorsById": {
				"super black": {
					"id": "super black",
					"label": "SUPER BLACK",
					"spriteIndex": 0,
					"mediaIds": [
						"6_100955206",
						"5_100955205"
					],
					"standardColors": [
						"Black"
					],
					"swatchMediaId": "6_100955206"
				}
			},
			"colorIds": [
				"super black"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"5_100955205": {
					"id": "5_100955205",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/5/_100955205.jpg"
				},
				"6_100955206": {
					"id": "6_100955206",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/6/_100955206.jpg"
				}
			},
			"name": "AG Everett SUD Slim Straight Fit Pants",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "188.00",
					"maxItemPrice": "188.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "131.60",
					"maxItemPrice": "131.60",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-everett-sud-slim-straight-fit-pants/5743201",
			"reviewCount": 176,
			"reviewStarRating": 4.8,
			"storeAvailability": null
		},
		"5743202": {
			"id": 5743202,
			"brandId": 1250,
			"brandName": "AG",
			"styleNumber": "5376588_2",
			"colorCount": 2,
			"colorDefaultId": "parched trail",
			"colorSpriteUrl": "https://n.nordstrommedia.com/swatchsprite.jpg?photos=10_106539690-11_106574131",
			"colorsById": {
				"florence fog": {
					"id": "florence fog",
					"label": "FLORENCE FOG",
					"spriteIndex": 1,
					"mediaIds": [
						"11_106574131",
						"10_106574190"
					],
					"standardColors": [
						"Metallic"
					],
					"swatchMediaId": "11_106574131"
				},
				"parched trail": {
					"id": "parched trail",
					"label": "PARCHED TRAIL",
					"spriteIndex": 0,
					"mediaIds": [
						"10_106539690",
						"9_106539709"
					],
					"standardColors": [
						"Beige"
					],
					"swatchMediaId": "10_106539690"
				}
			},
			"colorIds": [
				"parched trail",
				"florence fog"
			],
			"enticementIds": [
				"newMarkdown"
			],
			"enticements": null,
			"isBeauty": false,
			"isNordstromMade": false,
			"isOutfit": false,
			"isFeatured": false,
			"isUmap": false,
			"mediaById": {
				"10_106539690": {
					"id": "10_106539690",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106539690.jpg"
				},
				"10_106574190": {
					"id": "10_106574190",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/10/_106574190.jpg"
				},
				"11_106574131": {
					"id": "11_106574131",
					"group": "swatch",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/11/_106574131.jpg"
				},
				"9_106539709": {
					"id": "9_106539709",
					"group": "main",
					"type": "image",
					"src": "https://n.nordstrommedia.com/ImageGallery/store/product/Zoom/9/_106539709.jpg"
				}
			},
			"name": "AG Wanderer Modern Slim Fit Shorts",
			"priceCurrencyCode": "USD",
			"priceCountryCode": "BD",
			"pricesById": {
				"original": {
					"id": "original",
					"minItemPercentOff": 0,
					"maxItemPercentOff": 0,
					"minItemPrice": "125.00",
					"maxItemPrice": "125.00",
					"priceValidUntilDate": null
				},
				"sale": {
					"id": "sale",
					"minItemPercentOff": 30,
					"maxItemPercentOff": 30,
					"minItemPrice": "87.50",
					"maxItemPrice": "87.50",
					"priceValidUntilDate": null
				}
			},
			"productPageUrl": "/s/ag-wanderer-modern-slim-fit-shorts/5743202",
			"reviewCount": 72,
			"reviewStarRating": 4.7,
			"storeAvailability": null
		}
	}]
}"""

to_py = json.loads(my_json)

base_url = "https://www.nordstrom.com"
product_list = []
not_downloaded = []
for product_id in to_py['productsById']:

    for key in product_id:
        images =[]
        name = product_id[key]['name']
        brand = product_id[key]['brandName']
        colors = product_id[key]['colorCount']
        url = base_url + product_id[key]['productPageUrl']
        price = "$"+product_id[key]["pricesById"]["original"]["minItemPrice"]


        for media_id in product_id[key]['mediaById']:
            images.append( product_id[key]['mediaById'][media_id]['src'])

        my_path = f'\\images\\nordstorm\\men\\{name}'
        file_path = dir_path + my_path
        for image in images:
            try:
                if not os.path.exists(file_path):
                    try:
                        os.makedirs(file_path)
                    except:
                        print("cant create folder ")
                urllib.request.urlretrieve(image,
                                           os.path.join(file_path, os.path.basename((image + '.jpg'))))
                print("image downloaded")
            except:
                not_downloaded.append(image)
        product = {
            'Name'    : name,
            'Category': "Men",
            'Price'   : price,
            'Url' : url,
        }
        product_list.append(product)
        print(f"-------------------------------------------done {name}--------------------------------------")

df = pd.DataFrame(product_list, columns=['Name', 'Category', 'Price', "Url"])
df.to_excel(dir_path + f"\\images\\nordstorm\\nordstorm_men.xlsx", index=False)

df = pd.DataFrame(not_downloaded, columns=['Name'])
df.to_excel(dir_path + f"\\images\\nordstorm\\nordstorm_men_not_downloaded.xlsx", index=False)
print(f"DONE nordstorm_men")

