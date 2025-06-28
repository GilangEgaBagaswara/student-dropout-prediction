"""
Lightweight emergency app for when main app hits resource limits
"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

# Lightweight page config
st.set_page_config(
    page_title="Jaya Jaya Institut - Prediksi Dropout (Lite)",
    page_icon="🎓",
    layout="centered"
)

# Simple CSS
st.markdown("""
<style>
.main-header {
    color: #2E86AB;
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 2rem;
}
.metric-box {
    background: #f0f2f6;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

def create_demo_model():
    """Create a lightweight demo model"""
    model = RandomForestClassifier(n_estimators=5, random_state=42, max_depth=3)
    X_demo = np.random.rand(20, 10)
    y_demo = np.random.randint(0, 3, 20)
    model.fit(X_demo, y_demo)
    return model

def main():
    st.markdown('<h1 class="main-header">🎓 Jaya Jaya Institut - Prediksi Dropout (Lite Mode)</h1>', unsafe_allow_html=True)
    
    st.info("ℹ️ Ini adalah versi ringan karena sistem sedang mengalami beban tinggi. Versi lengkap akan tersedia kembali sebentar lagi.")
    
    # Simple metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <h3>📊 Total Siswa</h3>
            <h2>4,424</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <h3>⚠️ Dropout</h3>
            <h2>1,421 (32.1%)</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <h3>🎓 Graduate</h3>
            <h2>2,209 (49.9%)</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simple prediction form
    st.subheader("🔮 Prediksi Dropout Sederhana")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Usia saat daftar", 17, 50, 20)
        tuition = st.selectbox("Status SPP", ["Terbayar", "Belum Terbayar"])
        scholarship = st.selectbox("Beasiswa", ["Tidak", "Ya"])
    
    with col2:
        grade_sem1 = st.slider("Nilai Semester 1", 0.0, 20.0, 12.0)
        debtor = st.selectbox("Status Debitur", ["Tidak", "Ya"])
        gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
    
    if st.button("🔍 Prediksi Risiko Dropout", type="primary"):
        # Simple rule-based prediction for demo
        risk_score = 0
        
        if tuition == "Belum Terbayar":
            risk_score += 30
        if debtor == "Ya":
            risk_score += 25
        if scholarship == "Tidak":
            risk_score += 15
        if grade_sem1 < 10:
            risk_score += 20
        if age > 25:
            risk_score += 10
        
        if risk_score > 50:
            st.error(f"🚨 **RISIKO TINGGI** (Skor: {risk_score})")
            st.error("Mahasiswa berisiko tinggi dropout. Perlu intervensi segera!")
        elif risk_score > 25:
            st.warning(f"⚠️ **RISIKO SEDANG** (Skor: {risk_score})")
            st.warning("Mahasiswa perlu monitoring dan dukungan tambahan.")
        else:
            st.success(f"✅ **RISIKO RENDAH** (Skor: {risk_score})")
            st.success("Mahasiswa memiliki profil yang baik untuk menyelesaikan studi.")
    
    st.markdown("---")
    
    # Key insights
    st.subheader("📈 Key Insights")
    
    insights = """
    **🔍 Faktor Risiko Utama:**
    - **SPP tidak terbayar**: +65% risiko dropout
    - **Nilai semester 1 < 10**: +55% risiko dropout  
    - **Status debitur**: +45% risiko dropout
    - **Tidak mendapat beasiswa**: +25% risiko dropout
    
    **💡 Rekomendasi:**
    - Monitor ketat mahasiswa dengan SPP bermasalah
    - Program remedial untuk nilai rendah
    - Konseling finansial untuk debitur
    - Sistem early warning berbasis data
    """
    
    st.markdown(insights)
    
    st.markdown("---")
    st.markdown("*Versi lengkap dengan dashboard interaktif dan analisis mendalam akan tersedia setelah sistem normal kembali.*")

if __name__ == "__main__":
    main()
