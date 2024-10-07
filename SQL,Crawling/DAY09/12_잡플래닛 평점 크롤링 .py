#--> 해댕 회사의 Jobplanet  페이지로 이동  


















for	key	in	xpath_dict.keys():
								#	전체 6개의 평점 가져오기
point=driver.find_element(By.XPATH,	xpath_dict.get(key)).text
print(f'{key}:	{point}',	end='	')
score_list.append(point)


#회사 6개 추가 





compary_score_dict[company_name]	=	score_list

# 딕셔너리로 리스트 저장



orient ='index' ==> 