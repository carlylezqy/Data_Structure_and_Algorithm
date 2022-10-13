#include <stdio.h>
#include <Windows.h>
#include <gdiplus.h>
#pragma comment(lib,"gdiplus.lib")

struct RGB //各ピクセルのRGB値を格納する構造体
{
	unsigned char R;
	unsigned char G;
	unsigned char B;
};

int main()
{
	//GdiPlusの有効化
	Gdiplus::GdiplusStartupInput Input;
	ULONG_PTR Token;
	Gdiplus::GdiplusStartup(&Token, &Input, NULL);

	int width = 0, height = 0; 

	Gdiplus::Bitmap image(L"image_1.jpg"); //画像の読み込み

	//画像の幅，高さの取得
	width = image.GetWidth();
	height = image.GetHeight();

	Gdiplus::Color pixelColor; //ピクセルの色情報を取得するためのColorクラスのインスタンスを作成

	// RGB構造体の2次元配列のため，取得した高さ，幅をもとにメモリ確保
	RGB** pixel = new RGB * [width];
	for (int i = 0; i < width; i++) {
		pixel[i] = new RGB[height];
	}

	//RGB値読み取り
	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			image.GetPixel(i, j, &pixelColor);
			pixel[i][j].R = pixelColor.GetR();
			pixel[i][j].G = pixelColor.GetG();
			pixel[i][j].B = pixelColor.GetB();
		}
	}

	//---------------------------------------------------------------------------------------
	// RGB値を１チャンネルに変換
	// GreyScale = 0.3R + 0.59G + 0.11B

	//グレースケールの輝度を格納する2次元配列の領域確保
	unsigned char** Grey = new unsigned char* [width];
	for (int i = 0; i < width; i++) {
		Grey[i] = new unsigned char[height];
	}

	//グレースケール輝度に変換
	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			RGB tmp = pixel[i][j];
			Grey[i][j] = 0.30 * tmp.R + 0.59 * tmp.G + 0.11 * tmp.B;
		}
	}

	//---------------------------------------------------------------------------------------
	// convert to Black and White pixels

	int* pixelnum = new int[256];
	for (int i = 0; i < 256; i++) {
		pixelnum[i] = 0;
	}

	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			pixelnum[Grey[i][j]]++;
		}
	}

	//白黒のしきい値を計算
	int temp = 0;
	unsigned char Threshold = 0;
	for (int i = 0; i < 256; i++) {
		temp += pixelnum[i];
		if (temp >= (width * height / 2)) {
			Threshold = i;
			break;
		}
	}

	printf("%d\n", Threshold);

	boolean** BW = new boolean * [width];
	for (int i = 0; i < width; i++) {
		BW[i] = new boolean[height];
	}

	//しきい値以上なら１，しきい値以下なら０
	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			if (Grey[i][j] >= Threshold) {
				BW[i][j] = 1;
			}
			else {
				BW[i][j] = 0;
			}
		}
	}


	//---------------------------------------------------------------------------------------
	// generate new image

	//255に０と１をかけることで，白か黒かに変換する
	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			Gdiplus::Color newpixel(255 * BW[i][j], 255 * BW[i][j], 255 * BW[i][j]);
			image.SetPixel(i, j, newpixel);
		}
	}

	//---------------------------------------------------------------------------------------
	// save image file in jpg format

	CLSID jpgClsid;
	CLSIDFromString(L"{557cf401-1a04-11d3-9a73-0000f81ef32e}", &jpgClsid);
	image.Save(L"out.jpg", &jpgClsid, NULL);

}