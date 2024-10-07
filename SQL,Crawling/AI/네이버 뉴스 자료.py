
# § datetime 변환
# • strptime(string,	format)
# – string을 datetime 객체로 변환: (p:	parse)
# • strftime(format)
# – datetime 객체를 string으로 변환:	(f:	format)

import	datetime


date_string =	'Tue,	13	Aug	2024	09:02:00 +0900'

#	strptime(string,	format):	string	->	datetime	변환
pdate =	datetime.datetime.strptime(date_string,	'%a,	%d	%b	%Y	%H:%M:%S	+0900')


print(type(pdate))
#	strftime(format):	datetime	->	string	변환


pdate_string =	pdate.strftime('%Y-%m-%d	%H:%M:%S')
print(type(pdate_string))
print(pdate_string)

import	urllib.request
import	datetime
import	json


def get_request_url(url):
    client_id = 'zsGUlCyQAMfwGr97CIDW'
    client_secret = "6ROZ3F95J_"

    req =urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",	client_id)
    req.add_header("X-Naver-Client-Secret",	client_secret)


    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
        
    except Exception as e :
        print(e)
        print(f'Error for URL : {url}')


# node#  -> 뉴스	
# search_text3# --> 인공지능


def get_naver_search(node, search_text,start , display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string =	f"{urllib.parse.quote(search_text)}"


    parameters =("?query={}&start={}&display={}".
                format(query_string,start,	display))
    
    url= base +node +parameters
    response = get_request_url(url)

    if response is None:
        return  None
    else:
        return json.loads(response)





def	get_post_data(post,	json_result_list,	cnt):
    title=post['title']
    description	=post['description']
    org_link =post['originallink']
    link=post['link']
    '''
    strptime()
    - %a:	abbreviated	weekday	name					
    - %b"	abbreviated	month	name
                    '''
    pdate =	datetime.datetime.strptime(post['pubDate'],	'%a,	%d	%b	%Y	%H:%M:%S	+0900')
    pdate =	pdate.strftime('%Y-%m-%d	%H:%M:%S')
    print(f"[{cnt}]",	end="	")
    print(title,	end=":	")
    print(pdate,	end="	")
    print(link)
    #	['번호',	'날짜',	'제목',	'개요',	'원본기사링크',	'네이버링크']
    json_result_list.append([cnt,	pdate,	title,	description,	org_link,	link])

def	main():
    node='news'		#	크롤링 대상
#	search_text =	input('검색어를 입력하세요:	')
    search_text ='AI 개발자 자격증'
    cnt =	0
    json_result_list =	[]

    json_response =get_naver_search(node,	search_text,	1,	10)
    while	(json_response is	not	None)	and	(json_response['display']!=	0):
        for	post	in	json_response['items']:
            cnt +=	1
            get_post_data(post,	json_result_list,	cnt)
        start=json_response['start']+json_response['display']
        json_response =	get_naver_search(node,	search_text,start,10)
    print(f'전체 검색 수:{cnt}')
				#	csv	파일로 저장
    #	['번호','날짜',	'제목',	'개요',	'원본기사링크',	'네이버링크']
    columns	=	['count',	'date',	'title',	'description',	'org_link',	'link']
    result_df =	pd.DataFrame(json_result_list,	columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv',	index=False,	encoding='utf-8')
				
if	__name__	==	'__main__':
    main()