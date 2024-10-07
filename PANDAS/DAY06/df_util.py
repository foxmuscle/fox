#-------------------------------------------------
# Series/DataFrame 으로 저장
#------------------------------------------------
# 함수기능 : DataFrame 의 기본정보와 속정 확인 기능
# 함수이름 : checkDataFrame
# 매개변수 : DataFrame 인스턴스 변수명 , DataFrame 인스턴스 이름
# 리턴값/반환값 : 없음
#-------------------------------------------------
def checkDataFrame(object, name):
    print(f'\n[{name}]')
    object.info()
    print(print(f'[index] : {object.index}'))
    print(f'[columns] : {object.columns}')
    print(f'[NDim]] : {object.ndim}')