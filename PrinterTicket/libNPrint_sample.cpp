#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <unistd.h>					// usleep
#include <iostream>
#include <fstream>
#include <time.h>					// localtime
#include <opencv2/core.hpp>			// for OpenCV3
#include <opencv2/highgui.hpp>		// for OpenCV3
#include <opencv2/imgcodecs.hpp>	// for OpenCV3
#define	N_SUCCESS					0
#define	N_ERR_OFFLINE				-5
#define IMG_RASTER_LINE				0x00
#define IMG_RASTER_BLOCK			0x01
#define IMG_RASTER_GRADATION		0x02
#define IMG_BITIMG					0x10
using namespace std;

typedef void(*NCALLBACK) (char*, int, int, int);
extern "C" int NEnumPrinters(char* o_printers, unsigned int* o_size);
extern "C" int NOpenPrinter(char* i_prt, unsigned char i_statusFlg, NCALLBACK i_callback);
extern "C" int NClosePrinter(char* i_prt);
extern "C" int NPrint(char* i_prt, char* i_dat, unsigned int i_size, unsigned int* o_jobid);
extern "C" int NDPrint(char* i_prt, unsigned char* i_dat, unsigned int i_size, unsigned int* o_jobid);
extern "C" int NImagePrint(char* i_prt, unsigned char* i_bmp, unsigned int i_width, unsigned int i_height, unsigned int i_channels, unsigned int i_step, unsigned char i_putType, unsigned int* o_jobid);
extern "C" int NImagePrintF(char* i_prt, char* i_bmp, unsigned char i_putType, unsigned int* o_jobid);
extern "C" int NGetStatus(char* i_prt, unsigned long* o_status);
extern "C" int NGetInformation(char* i_prt, unsigned char i_id, void* o_dat, unsigned long* o_time);
extern "C" int NStartDoc(char* i_prt, unsigned int* o_jobid);
extern "C" int NEndDoc(char* i_prt);
extern "C" int NCancelDoc(char* i_prt);
extern "C" unsigned long cputime();
extern "C" int NImagePrintWrap(char* i_prt, cv::Mat i_bmp, unsigned int i_width, unsigned int i_height, unsigned char i_putType, unsigned int* o_jobid);		// for OpenCV3

void fncGetDate(char *o_staData)
{
	time_t timep;
    struct tm *time_inf;
    char staDate[32];
    time(&timep);
    time_inf = localtime(&timep);
    memset(staDate, 0x00, 32);
    sprintf(staDate,"%02d/%02d/%04d %02d:%02d", time_inf->tm_mon + 1, time_inf->tm_mday, time_inf->tm_year + 1900, time_inf->tm_hour, time_inf->tm_min);
    memcpy(o_staData, staDate, strlen(staDate));
    return;
}

void fncTestSample(void)
{	
	ifstream Parameters;
	string CompanyNameSTR;
	string HeaderTextSTR;
	string AddressSTR;
	string CitySTR;
	string StateSTR;
	string CountrySTR;
	string TelephoneSTR;
	string MailSTR;
	string WebsiteSTR;
	string CashierIDSTR;
	string CardNumberSTR;
	string CurrencySTR;
	string PaymentMethodSTR;
	string PaymentInfoSTR;
	string CardPriceSTR;
	string LoadSTR;
	string SUBTOTALSTR;
	string IVASTR;
	string TOTALIVASTR;
	string TOTALSTR;
	string FootTextSTR;

	Parameters.open("Parameters.txt", ios::in);
	if(Parameters.fail()) {
		cout << "No se pudo abrir el archivo";
	}
	getline(Parameters, CompanyNameSTR);
	getline(Parameters, HeaderTextSTR);
	getline(Parameters, AddressSTR);
	getline(Parameters, CitySTR);
	getline(Parameters, StateSTR);
	getline(Parameters, CountrySTR);
	getline(Parameters, TelephoneSTR);
	getline(Parameters, MailSTR);
	getline(Parameters, WebsiteSTR);
	getline(Parameters, CashierIDSTR);
	getline(Parameters, CardNumberSTR);
	getline(Parameters, CurrencySTR);
	getline(Parameters, PaymentMethodSTR);
	getline(Parameters, PaymentInfoSTR);
	getline(Parameters, CardPriceSTR);
	getline(Parameters, LoadSTR);
	getline(Parameters, SUBTOTALSTR);
	getline(Parameters, IVASTR);
	getline(Parameters, TOTALIVASTR);
	getline(Parameters, TOTALSTR);
	getline(Parameters, FootTextSTR);
	Parameters.close();

	char CompanyName[36];
	char HeaderText[86];
	char Address[36];
	char City[36];
	char State[36];
	char Country[36];
	char Telephone[36];
	char Mail[36];
	char Website[36];
	char CashierID[36];
	char CardNumber[36];
	char Currency[36];
	char PaymentMethod[36];
	char PaymentInfo[86];
	char CardPrice[36];
	char Load[36];
	char SUBTOTAL[36]; 
	char IVA[36];
	char TOTALIVA[36];
	char TOTAL[36];
	char FootText[86];
	
	strcpy(CompanyName, CompanyNameSTR.c_str());
	strcpy(HeaderText, HeaderTextSTR.c_str());
	strcpy(Address, AddressSTR.c_str());
	strcpy(City, CitySTR.c_str());
	strcpy(State, StateSTR.c_str());
	strcpy(Country, CountrySTR.c_str());
	strcpy(Telephone, TelephoneSTR.c_str());
	strcpy(Mail, MailSTR.c_str());
	strcpy(Website, WebsiteSTR.c_str());
	strcpy(CashierID, CashierIDSTR.c_str());
	strcpy(CardNumber, CardNumberSTR.c_str());
	strcpy(PaymentMethod, PaymentMethodSTR.c_str());
	strcpy(PaymentInfo, PaymentInfoSTR.c_str());
	strcpy(Currency, CurrencySTR.c_str());
	strcpy(CardPrice, CardPriceSTR.c_str());
	strcpy(Load, LoadSTR.c_str());
	strcpy(SUBTOTAL, SUBTOTALSTR.c_str());
	strcpy(IVA, IVASTR.c_str());
	strcpy(TOTALIVA, TOTALIVASTR.c_str());
	strcpy(TOTAL, TOTALSTR.c_str());
	strcpy(FootText, FootTextSTR.c_str());

	char Temp[86];
	sprintf(Temp, "\"%s\"", CompanyName);
	strcpy(CompanyName, Temp);
	sprintf(Temp, "\"%s\"", HeaderText);
	strcpy(HeaderText, Temp);
	sprintf(Temp, "\"%s\"", Address);
	strcpy(Address, Temp);
	sprintf(Temp, "\"%s\"", City);
	strcpy(City, Temp);
	sprintf(Temp, "\"%s\"", State);
	strcpy(State, Temp);
	sprintf(Temp, "\"%s\"", Country);
	strcpy(Country, Temp);
	sprintf(Temp, "\"%s\"", Telephone);
	strcpy(Telephone, Temp);
	sprintf(Temp, "\"%s\"", Mail);
	strcpy(Mail, Temp);
	sprintf(Temp, "\"%s\"", Website);
	strcpy(Website, Temp);
	sprintf(Temp, "\"%s\"", CashierID);
	strcpy(CashierID, Temp);
	sprintf(Temp, "\"%s\"", CardNumber);
	strcpy(CardNumber, Temp);
	sprintf(Temp, "\"%s\"", Currency);
	strcpy(Currency, Temp);
	sprintf(Temp, "\"%s\"", PaymentMethod);
	strcpy(PaymentMethod, Temp);
	sprintf(Temp, "\"%s\"", PaymentInfo);
	strcpy(PaymentInfo, Temp);
	sprintf(Temp, "\"%s\"", CardPrice);
	strcpy(CardPrice, Temp);
	sprintf(Temp, "\"%s\"", Load);
	strcpy(Load, Temp);
	sprintf(Temp, "\"%s\"", SUBTOTAL);
	strcpy(SUBTOTAL, Temp);
	sprintf(Temp, "\"%s\"", IVA);
	strcpy(IVA, Temp);
	sprintf(Temp, "\"%s\"", TOTALIVA);
	strcpy(TOTALIVA, Temp);
	sprintf(Temp, "\"%s\"", TOTAL);
	strcpy(TOTAL, Temp);
	sprintf(Temp, "\"%s\"", FootText);
	strcpy(FootText, Temp);

	char staGetChr[8];
	char staPort[8] = "PRT001";
	char staDate[32];
	unsigned char rawGScmd[8];
	unsigned char rawGetData[128];
	int nmsRet;
	int nmsCnt;
	unsigned long nmuTimeout;
	unsigned long nmuTime;
	unsigned long nmuStatus;
	unsigned int nmuJob;
	unsigned int nmuGetJobID;
	unsigned int *pnmuID;

	char *staImgPath = "./PrintSample.jpg";
	cv::Mat img = cv::imread(staImgPath);

	printf("IMPRESION\n");
	
	nmsRet = NOpenPrinter("PRT001", 1, NULL);
	printf(" NOpenPrinter           ReturnCode : %d\n", nmsRet);
	if(nmsRet != N_SUCCESS)
	{
		exit(-1);
	}

	memset(staDate, 0x00, 32);
	strcat(staDate, "\"Date: ");
	fncGetDate(&staDate[strlen(staDate)]);
	strcat(staDate, "\"");

	nmsRet = NGetStatus(staPort, &nmuStatus);
	
	nmsRet = NPrint(staPort, "1b73021b73031b7304", strlen("1b73021b73031b7304"), &nmuJob);
	usleep(1000000);
	// Model name
	memset(rawGetData, 0x00, 128);
	nmsRet = NGetInformation(staPort, (unsigned char)0x02, rawGetData, &nmuTime);
	printf(" NGetInformation(ID:02) ReturnCode : %d -> Model Name       : %s\n", nmsRet, rawGetData);
	// Firmware version
	memset(rawGetData, 0x00, 128);
	nmsRet = NGetInformation(staPort, (unsigned char)0x03, rawGetData, &nmuTime);
	printf(" NGetInformation(ID:03) ReturnCode : %d -> Firmware Version : %s\n", nmsRet, rawGetData);
	// Boot version
	memset(rawGetData, 0x00, 128);
	nmsRet = NGetInformation(staPort, (unsigned char)0x04, rawGetData, &nmuTime);
	printf(" NGetInformation(ID:04) ReturnCode : %d -> Boot Version     : %s\n", nmsRet, rawGetData);

	// StartDoc
	nmuJob = 0;
	nmsRet = NStartDoc(staPort, &nmuJob);
	printf(" NStartDoc              ReturnCode : %d -> JOB ID : %d\n", nmsRet, nmuJob);
	if(nmsRet != N_SUCCESS)
	{
		exit(-1);
	}

	// 印字開始CMD
	// In printing command
	nmsCnt = 0;
	memset(rawGScmd, 0x00, 8);
	rawGScmd[nmsCnt++] = 0x1d;
	rawGScmd[nmsCnt++] = 0x47;
	rawGScmd[nmsCnt++] = 0x11;
	memcpy((unsigned long*)&rawGScmd[nmsCnt], &nmuJob, 4);
	nmsCnt+=4;
	nmsRet = NDPrint(staPort, rawGScmd, nmsCnt, NULL);

	nmsRet = NPrint(staPort, "1b61011b2130", strlen("1b61011b2130"), NULL); //LETRA GRANDE, NEGRITA Y CENTRADA


	// Raster image data
	nmsRet = NImagePrintF(staPort, staImgPath, IMG_RASTER_BLOCK, NULL);

	// Raster image data
	//nmsRet = NImagePrintWrap(staPort, img, img->width, img->height, IMG_RASTER_BLOCK, NULL);
	nmsRet = NImagePrintWrap(staPort, img, img.cols, img.rows, IMG_RASTER_BLOCK, NULL);

	// 文字データ
	// other data
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "1b61011b2130", strlen("1b61011b2130"), NULL); //LETRA GRANDE, NEGRITA Y CENTRADA
	nmsRet = NPrint(staPort, CompanyName, strlen(CompanyName), NULL);
	nmsRet = NPrint(staPort, "1b2100", strlen("1b2100"), NULL); //LETRA CHICA
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, HeaderText, strlen(HeaderText), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "1b6100", strlen("1b6100"), NULL); //POSICION DEL TEXTO A LA IZQUIERDA
	nmsRet = NPrint(staPort, "\"********************************\"0a", strlen("\"********************************\"0a"), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, Address, strlen(Address), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, City, strlen(City), NULL);
	nmsRet = NPrint(staPort, "\", \"", strlen("\", \""), NULL); //AGREGO COMA Y ESPACIO
	nmsRet = NPrint(staPort, State, strlen(State), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, Country, strlen(Country), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Tel: \"", strlen("\"Tel: \""), NULL); //AGREGO "Tel: "
	nmsRet = NPrint(staPort, Telephone, strlen(Telephone), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"E-Mail: \"", strlen("\"E-Mail: \""), NULL); //AGREGO "E-Mail: "
	nmsRet = NPrint(staPort, Mail, strlen(Mail), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Website: \"", strlen("\"Website: \""), NULL); //AGREGO "E-Mail: "
	nmsRet = NPrint(staPort, Website, strlen(Website), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"********************************\"0a", strlen("\"********************************\"0a"), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"CashierID: \"", strlen("\"CashierID: \""), NULL);
	nmsRet = NPrint(staPort, CashierID, strlen(CashierID), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, staDate, strlen(staDate), NULL);
	
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Card number: \"", strlen("\"Card number: \""), NULL);
	nmsRet = NPrint(staPort, CardNumber, strlen(CardNumber), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Payment method: \"", strlen("\"Payment method: \""), NULL);
	nmsRet = NPrint(staPort, PaymentMethod, strlen(PaymentMethod), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Payment info: \"", strlen("\"Payment info: \""), NULL);
	nmsRet = NPrint(staPort, PaymentInfo, strlen(PaymentInfo), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Card price: \"", strlen("\"Card price: \""), NULL);
	nmsRet = NPrint(staPort, Currency, strlen(Currency), NULL);
	nmsRet = NPrint(staPort, "\" \"", strlen("\" \""), NULL);
	nmsRet = NPrint(staPort, CardPrice, strlen(CardPrice), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"Load: \"", strlen("\"Load: \""), NULL);
	nmsRet = NPrint(staPort, Currency, strlen(Currency), NULL);
	nmsRet = NPrint(staPort, "\" \"", strlen("\" \""), NULL);
	nmsRet = NPrint(staPort, Load, strlen(Load), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"SUBTOTAL: \"", strlen("\"SUBTOTAL: \""), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, Currency, strlen(Currency), NULL);
	nmsRet = NPrint(staPort, "\" \"", strlen("\" \""), NULL);
	nmsRet = NPrint(staPort, SUBTOTAL, strlen(SUBTOTAL), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"IVA (%\"", strlen("\"IVA (%\""), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, IVA, strlen(IVA), NULL);
	nmsRet = NPrint(staPort, "\"): \"", strlen("\"): \""), NULL);
	nmsRet = NPrint(staPort, Currency, strlen(Currency), NULL);
	nmsRet = NPrint(staPort, "\" \"", strlen("\" \""), NULL);
	nmsRet = NPrint(staPort, TOTALIVA, strlen(TOTALIVA), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL);
	nmsRet = NPrint(staPort, "\"TOTAL: \"", strlen("\"TOTAL: \""), NULL);
	nmsRet = NPrint(staPort, Currency, strlen(Currency), NULL);
	nmsRet = NPrint(staPort, "\" \"", strlen("\" \""), NULL);
	nmsRet = NPrint(staPort, TOTAL, strlen(TOTAL), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"********************************\"0a", strlen("\"********************************\"0a"), NULL);
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "\"\"0a", strlen("\"\"0a"), NULL); //SALTO DE LINEA en el "0a"
	nmsRet = NPrint(staPort, "1b61011b2130", strlen("1b61011b2130"), NULL); //LETRA GRANDE, NEGRITA Y CENTRADA
	nmsRet = NPrint(staPort, "1b2100", strlen("1b2100"), NULL); //LETRA CHICA
	nmsRet = NPrint(staPort, FootText, strlen(FootText), NULL);

	

	// Feed / Cut command
	nmsRet = NPrint(staPort, "1b4aff1b69", strlen("1b4aff1b69"), NULL);

	// Binary Data
	nmsRet = NPrint(staPort, "<./rasterData.bin>", strlen("<./rasterData.bin>"), NULL);

	// Image Data
	nmsRet = NPrint(staPort, "[./PrintSample.jpg]", strlen("[./PrintSample.jpg]"), NULL);

	// Out printing command
	nmsRet = NPrint(staPort, "1d4710", strlen("1d4710"), NULL);

	// EndDoc
	nmsRet = NEndDoc(staPort);
	printf(" NEndDoc                ReturnCode : %d\n", nmsRet);
	if(nmsRet != N_SUCCESS)
	{
		nmsRet = NCancelDoc(staPort);
		printf(" NCancelDoc             ReturnCode : %d\n", nmsRet);
		exit(-1);
	}

	// 転送完了確認
	// It waits until forwarding is completed.
	nmuGetJobID = 0;
	nmuTimeout = cputime();
	while(nmuGetJobID != nmuJob)
	{
		memset(rawGetData, 0x00, 128);
		nmsRet = NGetInformation(staPort, (unsigned char)25, rawGetData, &nmuTime);
		pnmuID = (unsigned int*)&rawGetData;
		nmuGetJobID = *pnmuID;

		if(cputime() > (nmuTimeout+10000))
		{
			printf(" Print Error(ID:25)\n");
			break;
		}
	}
	printf(" ID:25 GetJobID:%d\n", nmuGetJobID);
	if(nmuGetJobID == nmuJob)
	{
		// 印刷完了待ち
		// It waits until printing is completed.
		nmuGetJobID = 0;
		nmuTimeout = cputime();
		while(nmuGetJobID != nmuJob)
		{
			memset(rawGetData, 0x00, 128);
			nmsRet = NGetInformation(staPort, (unsigned char)19, rawGetData, &nmuTime);
			pnmuID = (unsigned int*)&rawGetData;
			nmuGetJobID = *pnmuID;

			if(cputime() > (nmuTimeout+5000))
			{
				printf(" Print Error(ID:19)\n");
				break;
			}
		}
		if(nmuGetJobID == nmuJob)
		{
			printf(" ID:19 GetJobID:%d\n", nmuGetJobID);
			printf(" Print Success\n");
		}
	}
	
	// port close
	nmsRet = NClosePrinter(staPort);
	printf(" NClosePrinter          ReturnCode : %d\n", nmsRet);
	printf("Fin del modulo de impresion\n");
	return;
}

int main(void)
{
	int nmsRet;
	char staSelect[8];
	char *pPrinters;
	unsigned int nmuSize;
	unsigned int nmuDummy;

	printf("Inicio de la funcion de impresion\n");
	fncTestSample();
	printf("Fin del programa\n");
	return EXIT_SUCCESS;
}

//---------------------------------------------------------------------------
//  Name     : NImagePrintWrap
//  Detail   : Ver2.0以降のNImagePrint用のラッパー関数（for OpenCV2）
//             Wrapper function for NImagePrint after Ver2.0（for OpenCV2）
//  Argument : i_prt     : Printer name
//			　 i_bmp     : Image(OpenCV element)
//			　 i_width   : Image width
//			　 i_height  : Image height
//			　 i_putType : Output type
//						 :	0x00：Raster Line
//						 :  0x01：Raster Block
//						 :  0x02：Raster Block Gradation
//						 :  0x10：Bit image
//      	   o_jobid   : Print job id（Null can be specified）
//  Return   : Return value of NImagePrint
//---------------------------------------------------------------------------
/*
int NImagePrintWrap(char* i_prt, IplImage* i_bmp, unsigned int i_width, unsigned int i_height, unsigned char i_putType, unsigned int* o_jobid)
{
	int ret = N_SUCCESS;
	int channels = i_bmp->nChannels;			// Channel count of Image
	int step = i_bmp->widthStep;				// Step count of Image
	unsigned char* bufImage = i_bmp->imageData;	// Data array of Image

	ret = NImagePrint(i_prt, bufImage, i_width, i_height, channels, step, i_putType, o_jobid);

	return ret;
}
*/
//---------------------------------------------------------------------------
//  Name     : NImagePrintWrap
//  Detail   : Ver2.0以降のNImagePrint用のラッパー関数（for OpenCV3）
//             Wrapper function for NImagePrint after Ver2.0（for OpenCV3）
//  Argument : i_prt     : Printer name
//			　 i_bmp     : Image(OpenCV element)
//			　 i_width   : Image width
//			　 i_height  : Image height
//			　 i_putType : Output type
//						 :	0x00：Raster Line
//						 :  0x01：Raster Block
//						 :  0x02：Raster Block Gradation
//						 :  0x10：Bit image
//      	   o_jobid   : Print job id（Null can be specified）
//  Return   : Return value of NImagePrint
//---------------------------------------------------------------------------
 
int NImagePrintWrap(char* i_prt, cv::Mat i_bmp, unsigned int i_width, unsigned int i_height, unsigned char i_putType, unsigned int* o_jobid)
{
	int ret = N_SUCCESS;
	int channels = i_bmp.channels();			// Channel count of Image
	int step = i_bmp.step;						// Step count of Image
	unsigned char* bufImage = i_bmp.data;		// Data array of Image
	ret = NImagePrint(i_prt, bufImage, i_width, i_height, channels, step, i_putType, o_jobid);
	return ret;
}
