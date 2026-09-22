from flask import Flask,request,jsonify,send_from_directory
from faster_whisper import WhisperModel
import tempfile,os
B=os.path.dirname(os.path.abspath(__file__)); app=Flask(__name__); model=WhisperModel("small",device="cpu",compute_type="int8")
@app.get("/")
def home(): return send_from_directory(B,"index.html")
@app.get("/SONO-VIDZ-TRSC-logo.jpg")
def logo(): return send_from_directory(B,"SONO-VIDZ-TRSC-logo.jpg")
def tc(x):
 n=int(round(x*1000)); h=n//3600000;n%=3600000;m=n//60000;n%=60000;s=n//1000;ms=n%1000
 return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
@app.post("/transcribe")
def transcribe():
 if "file" not in request.files:return jsonify(error="NO FILE"),400
 f=request.files["file"]; with_tc=request.form.get("timecode")=="with"; ext=os.path.splitext(f.filename or "audio")[1]
 with tempfile.NamedTemporaryFile(delete=False,suffix=ext) as tmp:f.save(tmp.name);path=tmp.name
 try:
  segs,info=model.transcribe(path,beam_size=5,vad_filter=True); segs=list(segs)
  text="\n".join((f"[{tc(s.start)} → {tc(s.end)}] " if with_tc else "")+s.text.strip() for s in segs)
  return jsonify(text=text,language=info.language,timecode=with_tc)
 except Exception as e:return jsonify(error=str(e)),500
 finally:
  try:os.remove(path)
  except OSError:pass
if __name__=="__main__":app.run(host="127.0.0.1",port=8777,debug=False)
