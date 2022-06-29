#!/usr/bin/env python3


def Video_To_Audio_Converter_Tool(created_by="Ruben Leonardo Sigalingging."):
	import moviepy.editor as mp
	from os import system
	system("clear")
	system("pip install moviepy")
	system("pip install pyfiglet")
	system("clear")


	# Buat tampilan program lebih menarik.
	from pyfiglet import figlet_format
	tampilan=figlet_format("VTACT",font="slant")
	print(tampilan)
	print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Oleh: \033[91mRuben Leonardo Sigalingging.")
	print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Pada: \033[91mRabu, 29 Juni 2022, Pukul 12:05 PM.")
	print("\033[91m[\033[94m!\033[91m] \033[94mFungsi: \033[91mUntuk Mengkonversi File Video Ke Audio.\n")


	# Buat Input Untuk USER Menginputkan File Videonya,
	# Untuk Dikonversi Ke Audio (.MP3)
	file_video_kamu=input("\033[91m[\033[94m!\033[91m] \033[94mInput File Video Kamu: \033[91m\033[3m")


	# Cek Apakah File Video Yang Diinputkan User Ada Didalam Folder Yang Sama,
	# Dengan Kode Program Pengkonversi Ini.
	import os
	if os.path.isfile(file_video_kamu)==True:
		print("\n")
		print("\033[91m[\033[94m!\033[91m] \033[94mFile Tersebut \033[91mAda!")
	else:
		print("\n")
		print("\033[91m[\033[94m!\033[91m] \033[94mFile Tersebut \033[91mTidak Ada!")
		print("\n")

	konversi_file_video_kamu=mp.VideoFileClip(file_video_kamu)
	# Ubah Ke AUDIO (.MP3)
	nama_file_audio_hasil_konversi=input("\033[0m\033[91m[\033[0m\033[94m!\033[0m\033[91m] \033[0m\033[94mNama File Audio Yang Diinginkan: \033[0m\033[91m\033[3m")
	konversi_file_video_kamu.audio.write_audiofile(nama_file_audio_hasil_konversi)
Video_To_Audio_Converter_Tool()