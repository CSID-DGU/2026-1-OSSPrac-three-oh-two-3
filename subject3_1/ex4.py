from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
       result=dict()
       result['Name']=request.form.get('Name')
       
       # 추가: 체크박스 여러개 → join으로 문자열 변환
       result['languages'] =  ','.join(request.form.getlist('languages'))  
       
       return render_template('result.html',result=result)

if __name__ =='__main__':
     app.run(debug=True)
