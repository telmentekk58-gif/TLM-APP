import streamlit as st
from google import genai

# 1. Google Gemini AI холболт
# Өөрийн урт API түлхүүрээ доорх хашилтан дотор заавал тавиарай!
API_KEY = "ЯГ ЭНД ТҮЛХҮҮРЭЭ БУЦААЖ ТАВИАРАЙ"

client = genai.Client(api_key=API_KEY)

# 2. Вэбсайтны толгой хэсэг
st.set_page_config(page_title="AI Career Guide", page_icon="🎯")
st.title("🎯 Ирээдүйн Мэргэжил Сонголтын AI Туслах")
st.write("Таны сонирхол, давуу талд тулгуурлан хамгийн ирээдүйтэй мэргэжлийг Gemini AI бодож олно.")

# 3. Хэрэглэгчийн оролт
user_name = st.text_input("Таны нэр хэн бэ?", placeholder="Энд нэрээ бичнэ үү...")
user_interest = st.text_input("Та юу сонирхдог вэ? (Жишээ нь: зураг зурах, тоглоом тоглох, математик, спорт...)", placeholder="Сонирхлоо дэлгэрэнгүй бичвэл AI илүү гоё хариулна...")

# 4. AI ажиллах хэсэг
if st.button("Ирээдүйг шинжлэх 🧠"):
    if user_name and user_interest:
        with st.spinner("Gemini AI танд зориулж мэргэжил сонголтыг тооцоолж байна..."):
            try:
                # Систем гацахгүй байх үүднээс зааврыг англиар өгөв (Гэхдээ монголоор хариулна)
                prompt_text = f"The user's name is {user_name}. Their interest is: {user_interest}. Based on this, provide a creative and encouraging career advice in Mongolian language. Format the response beautifully with paragraphs."
                
                # Gemini модель руу илгээх
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt_text,
                )
                
                # Хариултыг дэлгэцэнд харуулах
                st.balloons()
                st.success(f"✨ {user_name}-д зориулсан AI дүн шинжилгээ бэлэн боллоо!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"AI холболтонд алдаа гарлаа: {e}")
    else:
        st.error("⚠️ Хөтөч ажиллуулахын тулд нэр болон сонирхлоо заавал бичнэ үү!")
