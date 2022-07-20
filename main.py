from lib.anime import *
from lib.brainly import *
from lib.manga import *
from lib.resize import *
from lib.search import *
from lib.nulis import *
from urllib.parse import *
from flask import *
from bs4 import BeautifulSoup as bs
from requests import get, post
import os, math, json, random, re, html_text, pytesseract, base64, time

ua_ig = 'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)'

app = Flask(__name__)
apiKey = 'O8mUD3YrHIy9KM1fMRjamw8eg'
apiKey_ocr = '09731daace88957'
app.config['MEDIA'] = 'tts'
app.secret_key = b'BB,^z\x90\x88?\xcf\xbb'

def convert_size(size_bytes):
	if size_bytes == 0:
		return '0B'
	size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return '%s %s' % (s, size_name[i])

@app.route('/tts/<path:filename>', methods=['GET','POST'])
def sendTts(filename):
	return send_from_directory(app.config['MEDIA'], filename, as_attachment=True)

@app.route('/api/layer', methods=['GET','POST'])
def layer():
	if request.args.get('base64image'):
		try:
			open('piw.jpg','w').write(request.args.get('base64image'))
			os.system('base64 -i -d piw.jpg > paw.jpg')
			hehe = resizeTo('paw.jpg')
			huhu = layer(hehe, 'black')
			os.system('base64 result.jpg > pow.jpg')
			return {
				'status': 200,
				'result': '`data:image/jpg;base64,%s`' % open('pow.jpg').read()
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[!] Invalid base64 image!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter base64image'
		}
@app.route('/api/spamcall', methods=['GET','POST'])
def spamcall():
    if request.args.get('no'):
        no = request.args.get('no')
        if str(no).startswith('8'):
            hasil = ''
            kyaa = post('https://id.jagreward.com/member/verify-mobile/%s' % no).json()
            print(kyaa['message'])
            if 'Anda akan menerima' in kyaa['message']:
                hasil += '[!] Berhasil mengirim spam call ke nomor : 62%s' % no
            else:
                hasil += '[!] Gagal mengirim spam call ke nomor : 62%s' % no
            return {
                'status': 200,
                'logs': hasil
            }
        else:
            return {
                'status': False,
                'msg': '[!] Tolong masukkan nomor dengan awalan 8'
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter no' 
        }
@app.route('/nulis', methods=['GET','POST'])
def noolees():
    if request.args.get('text'):
        try:
            nulis = tulis(unquote(request.args.get('text')))
            for i in nulis:
                i.save('resolt.jpg')
            return {
                'status': 200,
                'result': imageToBase64('resolt.jpg')
            }
        except:
            return {
                'status': False,
                'error': 'Failed writing dude:('
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter text'
        }
@app.route('/api/wiki', methods=['GET','POST'])
def wikipedia():
	if request.args.get('q'):
		try:
			kya = request.args.get('q')
			cih = f'https://id.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={kya}'
			heuh = get(cih).json()
			heuh_ = heuh['query']['pages']
			hueh = re.findall(r'(\d+)', str(heuh_))
			result = heuh_[hueh[0]]['extract']
			return {
				'status': 200,
				'result': result
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Yang anda cari tidak bisa saya temukan di wikipedia!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan param q'
		}

@app.route('/api/tts', methods=['GET','POST'])
def tts():
	if request.args.get('text'):
		try:
			teks = request.args.get('text')
			print(teks)
			if int(len(teks)) - int(len(teks.split(' '))) == 250:
				return {
					'status': 200,
					'msg': '[❗] Maaf teks terlalu panjang!!',
				}
			else:
				url = f'https://rest.farzain.com/api/tts.php?id={teks}&apikey='
				if os.path.isfile('./tts/tts.mp3') == True:
					os.remove('./tts/tts.mp3')
					Tts = get(f'{url}{apiKey}').content
					open('tts/tts.mp3','wb').write(Tts)
					return {
						'status': 200,
						'msg': 'Success convert text to speech!',
						'file': 'https://mhankbarbar/tts/tts.mp3'
					}
				else:
					Tts = get(f'{url}{apiKey}').content
					open('tts/tts.mp3','wb').write(Tts)
					return {
						'status': 200,
						'msg': 'Success convert text to speech!',
						'file': 'https://mhankbarbar.herokuapp.com/tts/tts.mp3'
					}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'msg': '[!] Upss, terjadi kesalahan'
			}
	else:
		return {
			'status': 200,
			'msg': '[!] Masukkan parameter text'
		}

@app.route('/api/ig', methods=['GET','POST'])
def keepsaveitig():
	if request.args.get('url'):
		try:
			urlvideo3 = request.args.get('url')
			cuih3 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo3}'
			hedeh3 = get(cuih3).json()
			hedeh3_ = hedeh3 ['response']['links']
			result3 = hedeh3_
			return {
				'status': 200,
				'result': result3
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/twitter', methods=['GET','POST'])
def keepsaveittwitter():
	if request.args.get('url'):
		try:
			urlvideo1 = request.args.get('url')
			cuih1 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo1}'
			hedeh1 = get(cuih1).json()
			hedeh1_ = hedeh1['response']
			result1 = hedeh1_
			return {
				'status': 200,
				'result': result1
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/9gag', methods=['GET','POST'])
def keepsaveit9gag():
	if request.args.get('url'):
		try:
			urlvideo2 = request.args.get('url')
			cuih2 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo2}'
			hedeh2 = get(cuih2).json()
			hedeh2_ = hedeh2['response']
			result2 = hedeh2_
			return {
				'status': 200,
				'result': result2
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/like', methods=['GET','POST'])
def keepsaveitlike():
	if request.args.get('url'):
		try:
			urlvideo4 = request.args.get('url')
			cuih4 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo4}'
			hedeh4 = get(cuih4).json()
			hedeh4_ = hedeh4['response']
			result4 = hedeh4_
			return {
				'status': 200,
				'result': result4
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/vimeo', methods=['GET','POST'])
def keepsaveitvimeo():
	if request.args.get('url'):
		try:
			urlvideo5 = request.args.get('url')
			cuih5 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo5}'
			hedeh5 = get(cuih5).json()
			hedeh5_ = hedeh5['response']
			result5 = hedeh5_
			return {
				'status': 200,
				'result': result5
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/wwe', methods=['GET','POST'])
def keepsaveitwwe():
	if request.args.get('url'):
		try:
			urlvideo6 = request.args.get('url')
			cuih6 = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo6}'
			hedeh6 = get(cuih6).json()
			hedeh6_ = hedeh6['response']
			result6 = hedeh6_
			return {
				'status': 200,
				'result': result6
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}
	
@app.route('/api/ytv', methods=['GET','POST'])
def ytv():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			ytv = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(ytv['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-23].text
			id = re.findall('var k__id = "(.*?)"', ytv['result'])
			thumb = bs(ytv['result'], 'html.parser').find('img')['src']
			title = bs(ytv['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp4','fquality':'360p'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'title': title,
				'thumb': thumb,
				'result': dl_link,
				'resolution': '360p',
				'filesize': filesize,
				'ext': 'mp4'
			}
		except Exception as e:
			print('Error : %s ' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan, mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': 'Masukkan parameter url'
		}

@app.route('/api/yta', methods=['GET','POST'])
def yta():
	if request.args.get('url'):
		try:
			url = request.args.get('url').replace('[','').replace(']','')
			yta = post('https://www.y2mate.com/mates/en60/analyze/ajax',data={'url':url,'q_auto':'0','ajax':'1'}).json()
			yaha = bs(yta['result'], 'html.parser').findAll('td')
			filesize = yaha[len(yaha)-10].text
			id = re.findall('var k__id = "(.*?)"', yta['result'])
			thumb = bs(yta['result'], 'html.parser').find('img')['src']
			title = bs(yta['result'], 'html.parser').find('b').text
			dl_link = bs(post('https://www.y2mate.com/mates/en60/convert',data={'type':url.split('/')[2],'_id':id[0],'v_id':url.split('/')[3],'ajax':'1','token':'','ftype':'mp3','fquality':'128'}).json()['result'],'html.parser').find('a')['href']
			return {
				'status': 200,
				'title': title,
				'thumb': thumb,
				'filesize': filesize,
				'result': dl_link,
				'ext': 'mp3'
			}
		except Exception as e:
			print('Error : %s' % e)
			return {
				'status': False,
				'error': '[❗] Terjadi kesalahan mungkin link yang anda kirim tidak valid!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/chord', methods=['GET','POST'])
def chord():
	if request.args.get('q'):
		try:
			q = request.args.get('q').replace(' ','+')
			id = get('http://app.chordindonesia.com/?json=get_search_results&exclude=date,modified,attachments,comment_count,comment_status,thumbnail,thumbnail_images,author,excerpt,content,categories,tags,comments,custom_fields&search=%s' % q).json()['posts'][0]['id']
			chord = get('http://app.chordindonesia.com/?json=get_post&id=%s' % id).json()
			result = html_text.parse_html(chord['post']['content']).text_content()
			return {
				'status': 200,
				'result': result
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Maaf chord yang anda cari tidak dapat saya temukan!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/komiku', methods=['GET','POST'])
def komiku():
    if request.args.get('q'):
        try:
            q = request.args.get('q')
            komi = search_komiku(q)
            if 'Tidak di temukan' not in komi:
                manga = scrap_komiku(komi)
                return {
                    'status': 200,
                    'info': manga['info'],
                    'genre': manga['genre'],
                    'sinopsis': manga['sinopsis'],
                    'thumb': manga['thumb'],
                    'link_dl': manga['dl_link']
                }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Manga %s Tidak di temukan' % unquote(q)
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter q'
        }

@app.route('/api/kuso', methods=['GET','POST'])
def kusonime():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_kusonime(quote(q))
			kuso=scrap_kusonime(he)
			if he != '':
				return {
					'status': 200,
					'sinopsis': kuso['sinopsis'],
					'thumb': kuso['thumb'],
					'info': kuso['info'],
					'title': kuso['title'],
					'link_dl': kuso['link_dl']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}
@app.route('/api/lk21', methods=['GET','POST'])
def lk21():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			he=search_lk21(quote(q))
			lk211=scrap_lk21(he)
			if he != '':
				return {
					'status': 200,
					'result_dl': lk211['result_dl'],
					'thumb': lk211['thumb'],
                    'sinopsis': lk211['sinopsis'],
                    'title': lk211['title']
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': 'Anime %s Tidak di temukan' % unquote(q)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/otakudesu')
def otakudesuu():
    if request.args.get('q'):
        try:
            q = request.args.get('q')
            he=search_otakudesu(quote(q))
            if he != '':
                otaku=scrap_otakudesu(he)
                return {
                    'status': 200,
                    'sinopsis': otaku['sinopsis'],
                    'thumb': otaku['thumb'],
                    'info': otaku['info'],
                    'title': otaku['title']
                }
        except Exception as e:
            print(e)
            return {
                'status': False,
                'error': 'Anime %s Tidak di temukan' % unquote(q)
            }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter q'
        }
            
@app.route('/api/brainly', methods=['GET','POST'])
def brainly_scraper():
	if request.args.get('q'):
		try:
			query = request.args.get('q')
			br=brainly(gsearch('"%s" site:brainly.co.id' % quote(query), lang='id')[0])
			return {
				'status': 200,
				'result': br
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Pertanyaan %s tidak dapat saya temukan di brainly' % unquote(query)
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/nekonime', methods=['GET','POST'])
def nekonimek():
	try:
		neko = get('https://waifu.pics/api/sfw/neko').json()
		nimek = neko['url']
		return {
			'status': 200,
			'result': nimek
		}
	except:
		neko = get('https://waifu.pics/api/sfw/neko').json()
		nimek = neko['url']
		return {
			'status': 200,
			'result': nimek
		}

@app.route('/api/stalk', methods=['GET','POST'])
def stalk():
	if request.args.get('username'):
		try:
			username = request.args.get('username').replace('@','')
			igestalk = bs(get('https://www.mystalk.net/profile/%s' % username, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36'}).text, 'html.parser').find('div', class_='user-profile-area')
			igestalk_ = igestalk.findAll('span')
			thumb = igestalk.find('img')['src']
			return {
				'status': 200,
				'Name': igestalk_[0].text.strip(),
				'Username': igestalk_[1].text.strip(),
				'Jumlah_Post': igestalk_[2].text.replace('\n',' ').strip(),
				'Jumlah_Followers': igestalk_[3].text.replace('\n',' ').strip(),
				'Jumlah_Following': igestalk_[4].text.replace('\n',' ').strip(),
				'Biodata': igestalk.find('p').text.strip(),
				'Profile_pic': thumb
			}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'error': '[❗] Username salah!!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter username'
		}

@app.route('/daerah', methods=['GET','POST'])
def daerah():
	daerah = 'Andreas, Ambon, Amlapura, Alford, Argamakmur, Atambua, Babo, Bagan Siapiapi, Central Kalimantan, Birmingham, Samosir, Balikpapan, Banda Aceh, Bandar Lampung, Bandung, Bangkalan, Cianjur, Bangko, Bangli, Banjar, Banjar Baru, Banjarmasin, Corn, BANTAENG , Banten, Bantul, Banyuwangi, Barabai, Barito, Barru, Batam, Batang, Batu, Baturaja, Batusangkar, Baubau, Bekasi, Bengkalis, Bengkulu, Benteng, Biak, Bima, Binjai, Bireuen, Bitung, Blitar, Blora, Bogor, Bojonegoro , Bondowoso, Bontang, Boyolali, Brebes, Bukit Tinggi, Maluku, Bulukumba, Buntok, Cepu, Ciamis, Cianjur, Cibinong, Cilacap, Cilegon, Cimahi, Cirebon, Curup, Demak, Denpasar, Depok, Dili, Dompu, Donggala, Dumai, Ende, Enggano, Enrekang, Fakfak, Garut, Gianyar, Gombong, Gorontalo, Gresik, Gunung Sitoli, Indramayu, Jakarta Barat, Jakarta Pusat, Jakarta Selatan, Jakarta Timur, Jakarta Utara, Jambi,Jayapura, Jember, Jeneponto, Jepara, Jombang, Kabanjahe, Kalabahi, Kalianda, Kandangan, Karanganyar, Karawang, Kasungan, Kayuagung, Kebumen, Kediri, Kefamenanu, Kendal, Kendari, Kertosono, Ketapang, Kisaran, Klaten, Kolaka, Kota Baru Pulau Laut , Bumi Bumi, Kota Jantho, Kotamobagu, Kuala Kapuas, Kuala Kurun, Kuala Pembuang, Kuala Tungkal, Kudus, Kuningan, Kupang, Kutacane, Kutoarjo, Labuhan, Lahat, Lamongan, Langsa, Larantuka, Lawang, Lhoseumawe, Limboto, Lubuk Basung, Lubuk Linggau, Lubuk Pakam, Lubuk Sikaping, Lumajang, Luwuk, Madiun, Magelang, Magetan, Majalengka, Majene, Makale, Makassar, Malang, Mamuju, Manna, Manokwari, Marabahan, Maros, Martapura Kalsel, Sulsel, Masohi, Mataram, Maumere, Medan, Mempawah, Menado, Mentok, Merauke, Metro, Meulaboh, Mojokerto, Muara Bulian, Muara Bungo, Muara Enim, Muara Teweh, Muaro Sijunjung, Muntilan, Nabire,Negara, Nganjuk, Ngawi, Nunukan, Pacitan, Padang, Padang Panjang, Padang Sidempuan, Pagaralam, Painan, Palangkaraya, Palembang, Palopo, Palu, Pamekasan, Pandeglang, Pangka_, Pangkajene Sidenreng, Pangkalan Bun, Pangkalpinang, Panyabungan, Par_, Parepare, Pariaman, Pasuruan, Pati, Payakumbuh, Pekalongan, Pekan Baru, Pemalang, Pematangsiantar, Pendopo, Pinrang, Pleihari, Polewali, Pondok Gede, Ponorogo, Pontianak, Poso, Prabumulih, Praya, Probolinggo, Purbalingga, Purukcahu, Purwakarta, Purwodadigrobogan, Purwarta Purworejo, Putussibau, Raha, Rangkasbitung, Rantau, Rantauprapat, Rantepao, Rembang, Rengat, Ruteng, Sabang, Salatiga, Samarinda, Kalbar, Sampang, Sampit, Sanggau, Sawahlunto, Sekayu, Selong, Semarang, Sengkang, Serang, Serui, Sibolga, Sidikalang, Sidoarjo, Sigli, Singaparna, Singaraja, Singkawang, Sinjai, Sintang, Situbondo, Slawi,Sleman, Soasiu, Soe, Solo, Solok, Soreang, Sorong, Sragen, Stabat, Subang, Sukabumi, Sukoharjo, Sumbawa Besar, Sumedang, Sumenep, Sungai Liat, Sungai Penuh, Sungguminasa, Surabaya, Surakarta, Tabanan, Tahuna, Takalar, Takengon , Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli , Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaTakalar, Takengon, Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli, Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaTakalar, Takengon, Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli, Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, YogyakartaWonogiri, Wonosari, Wonosobo, YogyakartaWonogiri, Wonosari, Wonosobo, Yogyakarta'
	no = 1
	hasil = ''
	for i in daerah.split(','):
		hasil += '%s. %s\n' % (no, i)
		no += 1
	return {
		'status': 200,
		'result': hasil
	}

@app.route('/api/jadwalshalat', methods=['GET','POST'])
def jadwalshalat():
	if request.args.get('daerah'):
		try:
			daer = request.args.get('daerah')
			daerah = 'Ambarawa, Ambon, Amlapura, Amuntai, Argamakmur, Atambua, Babo, Bagan Siapiapi, Kalteng, Bajawa, Balige, Balikpapan, Banda Aceh, Bandarlampung, Bandung, Bangkalan, Bangkinang, Bangko, Bangli, Banjar, Banjar Baru, Banjarmasin, Banjarnegara, Bantaeng, Banten, Bantul, Banyuwangi, Barabai, Barito, Barru, Batam, Batang, Batu, Baturaja, Batusangkar, Baubau, Bekasi, Bengkalis, Bengkulu, Benteng, Biak, Bima, Binjai, Bireuen, Bitung, Blitar, Blora, Bogor, Bojonegoro, Bondowoso, Bontang, Boyolali, Brebes, Bukit Tinggi, Maluku, Bulukumba, Buntok, Cepu, Ciamis, Cianjur, Cibinong, Cilacap, Cilegon, Cimahi, Cirebon, Curup, Demak, Denpasar, Depok, Dili, Dompu, Donggala, Dumai, Ende, Enggano, Enrekang, Fakfak, Garut, Gianyar, Gombong, Gorontalo, Gresik, Gunung Sitoli, Indramayu, Jakarta Barat, Jakarta Pusat, Jakarta Selatan, Jakarta Timur, Jakarta Utara, Jambi, Jayapura, Jember, Jeneponto, Jepara, Jombang, Kabanjahe, Kalabahi, Kalianda, Kandangan, Karanganyar, Karawang, Kasungan, Kayuagung, Kebumen, Kediri, Kefamenanu, Kendal, Kendari, Kertosono, Ketapang, Kisaran, Klaten, Kolaka, Kota Baru Pulau Laut, Kota Bumi, Kota Jantho, Kotamobagu, Kuala Kapuas, Kuala Kurun, Kuala Pembuang, Kuala Tungkal, Kudus, Kuningan, Kupang, Kutacane, Kutoarjo, Labuhan, Lahat, Lamongan, Langsa, Larantuka, Lawang, Lhoseumawe, Limboto, Lubuk Basung, Lubuk Linggau, Lubuk Pakam, Lubuk Sikaping, Lumajang, Luwuk, Madiun, Magelang, Magetan, Majalengka, Majene, Makale, Makassar, Malang, Mamuju, Manna, Manokwari, Marabahan, Maros, Martapura Kalsel, Sulsel, Masohi, Mataram, Maumere, Medan, Mempawah, Menado, Mentok, Merauke, Metro, Meulaboh, Mojokerto, Muara Bulian, Muara Bungo, Muara Enim, Muara Teweh, Muaro Sijunjung, Muntilan, Nabire, Negara, Nganjuk, Ngawi, Nunukan, Pacitan, Padang, Padang Panjang, Padang Sidempuan, Pagaralam, Painan, Palangkaraya, Palembang, Palopo, Palu, Pamekasan, Pandeglang, Pangka_, Pangkajene Sidenreng, Pangkalan Bun, Pangkalpinang, Panyabungan, Par_, Parepare, Pariaman, Pasuruan, Pati, Payakumbuh, Pekalongan, Pekan Baru, Pemalang, Pematangsiantar, Pendopo, Pinrang, Pleihari, Polewali, Pondok Gede, Ponorogo, Pontianak, Poso, Prabumulih, Praya, Probolinggo, Purbalingga, Purukcahu, Purwakarta, Purwodadigrobogan, Purwokerto, Purworejo, Putussibau, Raha, Rangkasbitung, Rantau, Rantauprapat, Rantepao, Rembang, Rengat, Ruteng, Sabang, Salatiga, Samarinda, Kalbar, Sampang, Sampit, Sanggau, Sawahlunto, Sekayu, Selong, Semarang, Sengkang, Serang, Serui, Sibolga, Sidikalang, Sidoarjo, Sigli, Singaparna, Singaraja, Singkawang, Sinjai, Sintang, Situbondo, Slawi, Sleman, Soasiu, Soe, Solo, Solok, Soreang, Sorong, Sragen, Stabat, Subang, Sukabumi, Sukoharjo, Sumbawa Besar, Sumedang, Sumenep, Sungai Liat, Sungai Penuh, Sungguminasa, Surabaya, Surakarta, Tabanan, Tahuna, Takalar, Takengon, Tamiang Layang, Tanah Grogot, Tangerang, Tanjung Balai, Tanjung Enim, Tanjung Pandan, Tanjung Pinang, Tanjung Redep, Tanjung Selor, Tapak Tuan, Tarakan, Tarutung, Tasikmalaya, Tebing Tinggi, Tegal, Temanggung, Tembilahan, Tenggarong, Ternate, Tolitoli, Tondano, Trenggalek, Tual, Tuban, Tulung Agung, Ujung Berung, Ungaran, Waikabubak, Waingapu, Wamena, Watampone, Watansoppeng, Wates, Wonogiri, Wonosari, Wonosobo, Yogyakarta'
			url = f'http://docs-jojo.herokuapp.com/api/jadwalshalat?daerah={daer}'
			jadwal = get(url).json()
			return {
				'Imsyak': jadwal['Imsyak'],
				'Subuh': jadwal['Subuh'],
				'Dhuha': jadwal['Dhuha'],
				'Dzuhur': jadwal['Dzuhur'],
				'Ashar': jadwal['Ashar'],
				'Maghrib': jadwal['Maghrib'],
				'Isya': jadwal['Isya']
			}
		except:
			return {
				'status': False,
				'error': '[❗] Daerah yang tersedia hanya : %s' % daerah
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter daerah'
		}

@app.route('/api/infogempa', methods=['GET','POST'])
def infogempa():
	be = bs(get('https://www.bmkg.go.id/').text, 'html.parser').find('div', class_="col-md-4 md-margin-bottom-10")
	em = be.findAll('li')
	img = be.find('a')['href']
	return {
		'status': 200,
		'map': img,
		'waktu': em[0].text,
		'magnitude': em[1].text,
		'kedalaman': em[2].text,
		'koordinat': em[3].text,
		'lokasi': em[4].text,
		'potensi': em[5].text
	}

@app.route('/api/cuaca', methods=['GET','POST'])
def cuaca():
	if request.args.get('q'):
		try:
			q = request.args.get('q')
			print(q)
			url = f'https://rest.farzain.com/api/cuaca.php?id={q}&apikey='
			weather = get(f'{url}{apiKey}').json()
			print(weather)
			if weather['respon']['deskripsi'] == 'null' or weather['respon']['deskripsi'] == None:
				return {
					'status': 404,
					'error': '[❗] Gagal mengambil informasi cuaca, mungkin tempat tidak terdaftar/salah!'
				}
			else:
				return {
					'status': 200,
					'result': {
						'tempat': weather['respon']['tempat'],
						'cuaca': weather['respon']['cuaca'],
						'desk': weather['respon']['deskripsi'],
						'suhu': weather['respon']['suhu'],
						'kelembapan': weather['respon']['kelembapan'],
						'udara': weather['respon']['udara'],
						'angin': weather['respon']['angin']
					},
					'creator': 'Mhank BarBar'
				}
		except Exception as e:
			print('Error : %s' % e)
			return {
				'status': False,
				'msg': '[❗] Gagal mengambil informasi cuaca, mungkin tempat tidak terdaftar/salah!'
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter q'
		}

@app.route('/api/randomquotes', methods=['GET','POST'])
def quotes():
	quotes_file = json.loads(open('quotes.json').read())
	result = random.choice(quotes_file)
	print(result)
	return {
		'status': 200,
		'author': result['author'],
		'quotes': result['quotes']
	}
@app.route('/api/ig2', methods=['GET','POST'])
def keepsaveitig2():
	if request.args.get('url'):
		try:
			urlvideo = request.args.get('url')
			cuih = f'https://keepsaveit.com/api/?api_key=o3fLL3budzW6OmiuyXYHfp6nHx1S8vykAmWjLBOpJDgLqh5EM8&url={urlvideo}'
			hedeh = get(cuih).json()
			print(hedeh)
			if hedeh['response']['links'] == 'null' or hedeh['response']['links'] == None:
				return {
					'status': 404,
					'error': '[❗] Gagal mengambil informasi cuaca, mungkin tempat tidak terdaftar/salah!'
				}
			else:
				return {
					'links': hedeh['response']['links'],
					'thumb': hedeh['response']['thumbnail'],
					'title': hedeh['response']['title']					
				}
		except Exception as e:
			print(e)
			return {
				'status': False,
				'result': 'https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg',
				'error': True
			}
	else:
		return {
			'status': False,
			'msg': '[!] Masukkan parameter url'
		}

@app.route('/api/tebakgambar', methods=['GET','POST'])
def tebakgambar():
	tebakgambar_file = json.loads(open('tebakgambar.json', encoding='utf-8').read())
	result = random.choice(tebakgambar_file)
	print(result)
	return {
		'status': 200,
		'index': result['index'],
		'img': result['img'],
		'jawaban': result['jawaban'],
		'deskripsi': result['deskripsi']
	}

@app.route('/api/tebaklirik', methods=['GET','POST'])
def tebaklirik():
	tebaklirik_file = json.loads(open('tebaklirik.json').read())
	result = random.choice(tebaklirik_file)
	print(result)
	return {
		'status': 200,
		'soal': result['soal'],
		'jawaban': result['jawaban']
	}

@app.route('/api/quotesnime/random', methods=['GET','POST'])
def quotesnimerandom():
	quotesnime = get('https://animechan.vercel.app/api/random').json()
	print(quotesnime)
	return {
		'status': 200,
		'quote': quotesnime['quote'],
		'character': quotesnime['character'],
		'anime': quotesnime['anime']
	}

@app.route('/random', methods=['GET','POST'])
def r4ndom():
	return render_template('random.html')

@app.route('/islam', methods=['GET','POST'])
def islam():
	return render_template('islam.html')

@app.route('/game', methods=['GET','POST'])
def game():
	return render_template('game.html')

@app.route('/edukasi', methods=['GET','POST'])
def edukasi():
	return render_template('edukasi.html')

@app.route('/downloader', methods=['GET','POST'])
def downloader():
	return render_template('downloader.html')

@app.route('/api', methods=['GET','POST'])
def api():
	return render_template('api.html')

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.errorhandler(404)
def error(e):
	return render_template('error.html'), 404
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
