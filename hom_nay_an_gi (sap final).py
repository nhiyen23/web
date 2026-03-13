import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Hôm Nay Ăn Gì?",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    /* Import beautiful fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;500;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #fdfbfb 0%, #fff8f0 100%);
    }
    
    /* Navigation Bar Title */
    .navbar-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 1rem 0 2rem 0;
    }
    
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #fff5f0 0%, #ffe8d8 100%);
        border-radius: 30px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(255, 107, 107, 0.1);
    }
    
    .hero-title {
        text-align: center;
        font-family: 'Montserrat';
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title2 {
        font-family: 'Montserrat';
        font-size: 2.5rem;
        font-weight: 750;
        text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title3 {
        font-family: 'Montserrat';
        font-size: 1.8rem;
        font-weight: 730;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-family: 'Montserrat';
        font-size: 4rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 600;
        animation: fadeInDown 1s ease;
    }

    .hero-subtitle2 {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 700;
        animation: fadeInDown 1s ease;
    }
    
    .hero-description {
        font-family: 'Montserrat';
        font-size: 1.1rem;
        color: #777;
        max-width: 1000px;
        margin: 0 auto 2rem !important;
        line-height: 1.8;
        animation: fadeInDown 1s ease;
    }
    
    /* Buttons */
    .cta-button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 6px 25px rgba(255, 107, 107, 0.3);
        display: inline-block;
        margin: 0.5rem;
        text-decoration: none;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 35px rgba(255, 107, 107, 0.4);
    }
    
    .cta-button-secondary {
        background: white;
        color: #ff6b6b;
        border: 2px solid #ff6b6b;
    }
    
    /* Feature Cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 12px 14px;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
        margin-bottom: 24px;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15);
        border-color: #ff6b6b;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 6px;
        text-align: center;
    }
    
    .feature-title {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        font-weight: 650;
        color: #333;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .feature-description {
        font-family: 'Montserrat';
        color: #666;
        line-height: 1.6;
        text-align: center;
    }
    
    /* Restaurant Cards */
    .restaurant-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .restaurant-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.15);
        border-color: #ff6b6b;
    }
    
    .restaurant-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-address {
        font-family: 'DM Sans', sans-serif;
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-info {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .info-badge {
        background: linear-gradient(135deg, #fff5f0 0%, #ffe8d8 100%);
        color: #ff6b6b;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Section Titles */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: #333;
        margin: 3rem 0 2rem 0;
        text-align: center;
    }
    
    /* Filter Section */
    .filter-section {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 6px 25px rgba(255, 107, 107, 0.3);
    }
    
    .stats-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Team Cards */
    .team-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15);
    }
    
    .team-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        font-family: 'DM Sans', sans-serif;
        color: #ff6b6b;
        font-weight: 500;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #ffe8d8;
        font-family: 'DM Sans', sans-serif;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #ff6b6b;
        box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.1);
    }
    
    /* Streamlit Button Override */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Dữ liệu về quán ăn
restaurants_data = [
    {
        "name": "Quán Đức Quân",
        "address": "Số 2 Ngõ 84 Chùa Láng",
        "distance": "<500m",
        "price": "30-40k",
        "type": ["Bún/Phở/Miến/Bánh canh/Súp"],
        "time": ["Sáng", "Trưa", "Tối"],
        "hours": "5:00 - 0:00",
        "menu": [
            {"dish": "Bún chả nướng chấm-chan", "price": "35k"},
            {"dish": "Bún, miến, bánh đa trộn", "price": "35k"},
            {"dish": "Bún, miến, bánh đa riêu cua, cá, bò, mọc, chả lá lốt, thập cẩm", "price": "35k"}
        ],
        "reviews": [
            {"name": "Minh Anh", "rating": 5, "content": "Rất ngon!"},
            {"name": "Hoàng Long", "rating": 4, "content": "Phục vụ tốt."},
            {"name": "Thu Hà", "rating": 5, "content": "Sẽ quay lại!"}
        ]
    },
    {
        "name": "Cơm Thố Anh Nguyễn",
        "address": "Số 17 Chùa Láng",
        "phone": "0972489933",
        "distance": "220m",
        "price": "40-50k",
        "type": ["Cơm"],
        "time": ["Trưa", "Tối"],
        "hours": "9:45 - 21:45",
        "menu": [
          {"dish": "Cơm Thố Dương Châu", "price": "35k" },
          {"dish": "Cơm Thố Ốp La", "price": "35k" },
          {"dish": "Cơm Thố Gà", "price": "45k" },
          {"dish": "Cơm Thố Gà Quay", "price": "45k" },
          {"dish": "Cơm Thố Gà Nướng", "price": "45k", "tag": "Best seller top2" },
          {"dish": "Cơm Thố Bò", "price": "50k", "tag": "Best seller top3" },
          {"dish": "Cơm Thố Sườn Sụn", "price": "50k" },
          {"dish": "Cơm Thố Xá Xíu", "price": "50k", "tag": "Best seller top1" },
          {"dish": "Cơm Thố Gà + Xá Xíu", "price": "55k" },
          {"dish": "Cơm Thố Bò + Xá Xíu", "price": "60k" },
          {"dish": "Cơm Thố Bò + Gà", "price": "60k" },
          {"dish": "Cơm Thố Đặc Biệt (Bò + Gà + Xá Xíu + Trứng)", "price": "70k"}
        ],
        "reviews": [
            {"name": "Nguyễn Khánh Linh", "rating": 5, "content": "Ăn ổn, giá cả phù hợp, mới nhìn tưởng khẩu phần ít nhưng đến lúc ăn xong no ná thở, phải cố để không bỏ dở"},
            {"name": "Ngọc Tùng", "rating": 5, "content": "Đồ ăn ngon nha mọi người, mình đặt ship về đồ ăn vẫn nóng hổi"},
            {"name": "Nguyễn Đức Tài", "rating": 1, "content": "Khách đến chờ 15 phút đi ra mua đồ ăn bánh mì, nước uống quay lại vẫn chưa xong"}
        ]
    },
    {
        "name": "KOMTO",
        "address": "127 Ngõ 121/2 Chùa Láng",
        "phone": "0901020089",
        "distance": "150m",
        "price": "40-50k",
        "type": ["Cơm/Xôi/Cháo", "Gà/Thịt chiên"],
        "time": ["Trưa", "Tối"],
        "hours": "Mở đến 22:00",
        "menu": [
          { "dish": "Gà giòn sốt Thái (M)", "price": "40k" },
          { "dish": "Gà giòn sốt Thái (L)", "price": "50k" },
          { "dish": "Cơm đùi gà quế Lâm", "price": "50k" },
          { "dish": "Gà giòn sốt me (M)", "price": "40k" },
          { "dish": "Gà giòn sốt me (L)", "price": "50k" },
          { "dish": "Cơm đùi gà sốt me", "price": "50k" },
          { "dish": "Cơm gà giòn sốt mật ong (M)", "price": "40k" },
          { "dish": "Cơm gà giòn sốt mật ong (L)", "price": "50k" },
          { "dish": "Cơm heo Tứ Xuyên", "price": "50k" },
          { "dish": "Cơm gà sốt đặc biệt", "price": "40k" },
          { "dish": "Cơm gà nướng đặc biệt", "price": "45k" }
        ],
        "reviews": [
          {
            "name": "Thục Nghi",
            "rating": 4,
            "content": "Mình đi tầm 12h trưa quán siêu đông khách nên phục vụ hơi lâu nhưng đổi lại cơm ăn ngon, so với giá tầm 40-55k thì khẩu phần rất ổn. Canh ăn kèm free hơi nhạt, sốt Thái ổn, sốt me hợp chấm gà hơn."
          },
          {
            "name": "Công nhân pháp lý",
            "rating": 4,
            "content": "Tôi thề với ae, gọi phần gà không sốt thì giòn thật sự luôn. Phần cơm đặc biệt sốt làm gà không còn giòn nữa. KFC, Jollibee no door."
          }
        ]
     },
     {
        "name": "Kofuku - Tiệm cơm mì",
        "address": "2 Ngõ 106 Phố Chùa Láng",
        "distance": "220m",
        "price": "40-50k",
        "type": ["Cơm/Xôi/Cháo"],
        "time": ["Trưa", "Tối"],
        "hours": "10:00 - 14:00, 15:00 - 21:00",
        "menu": [
              { "dish": "Cơm Katsudon", "price": "55k" },
              { "dish": "Cơm gà Oyakodon", "price": "45k" },
              { "dish": "Cơm cari", "price": "35k" },
              { "dish": "Cơm cari Tonkatsu", "price": "55k" },
              { "dish": "Cơm gà Karaage", "price": "50k" },
              { "dish": "Cơm thịt heo Ontama", "price": "55k" },
              { "dish": "Cơm xá xíu", "price": "55k" },
              { "dish": "Cơm thịt heo Kimchi", "price": "55k" },
              { "dish": "Cơm thịt heo", "price": "50k" },
              { "dish": "Cơm cari tôm chiên", "price": "45k" },
              { "dish": "Cơm cari trứng ngâm tương", "price": "40k" },
              { "dish": "Trứng ngâm tương", "price": "8k/quả" },
              { "dish": "Trứng Ontama", "price": "8k/quả" },
              { "dish": "Kim chi", "price": "10k" },
              { "dish": "Tôm chiên", "price": "10k/3 con" },
              { "dish": "Tonkatsu", "price": "30k/cái" },
              { "dish": "Gà Karaage", "price": "30k/5 cái" },
              { "dish": "Trà tắc", "price": "10k" },
              { "dish": "Trà chanh", "price": "10k" },
              { "dish": "Trà bát bảo", "price": "10k" },
              { "dish": "Trà Olong", "price": "10k" },
              { "dish": "Coca", "price": "15k/lon" }
         ],
         "reviews": [
            {
              "name": "Linh Nhi",
              "rating": 4,
              "content": "Đông khách ở quán rất nhiều, cá nhân mình thấy cơm cà ri đáng thử nhất. Điểm trừ là quán bám mùi quần áo khá nặng, nhưng đồ ăn ngon nên chấp nhận."
            },
            {
              "name": "Nguyet Anh Le",
              "rating": 4,
              "content": "Quán nhỏ, buổi trưa rất đông, mình phải đợi khoảng 10 phút mới có chỗ. Cơm cà ri khá ngon, thịt không bị dai, khẩu phần vừa đủ. Nhân viên tận tình và giá rẻ hơn nhiều chỗ khác."
            },
            {
              "name": "Kim Ngân Trần",
              "rating": 5,
              "content": "Cơm cà ri tonkatsu ngon lắm, thịt chiên xù giòn, cơm dẻo. Giá sinh viên tầm 50–65k/món. Không gian hơi nhỏ."
            }
            ]
    }, 
  {
  "name": "Oanh Oanh - Xôi xéo - Gà tần",
  "address": "38 Nguyễn Chí Thanh",
  "distance": "750m",
  "price": "<30k",
  "type": ["Cơm/Xôi/Cháo"],
  "time": ["Sáng", "Trưa"],
  "hours": "10:00 - 22:00",
  "menu": [
      { "dish": "Xôi xéo hành mỡ đỗ", "price": "20k" },
      { "dish": "Xôi thập cẩm", "price": "45k" },
      { "dish": "Xôi gà nấm", "price": "25k-30k" },
      { "dish": "Xôi trứng thịt", "price": "25k-30k" },
      { "dish": "Xôi chả ruốc", "price": "25k-30k" },
      { "dish": "Xôi pate lạp xưởng", "price": "25k-30k" },
      { "dish": "Xôi da gà xốt chua cay", "price": "25k-30k" },
      { "dish": "Gà ác tần", "price": "65k" },
      { "dish": "Gà ta tần", "price": "65k" },
      { "dish": "Mì / miến gà tần", "price": "70k" },
      { "dish": "Mề tần", "price": "25k" },
      { "dish": "Chân gà tần", "price": "20k" },
      { "dish": "Trứng vịt lộn tần", "price": "10k/quả" }
  ],
  "reviews": [
    {
     "name": "Huyền Linh Vũ",
     "rating": 5,
     "content": "Quán rất cute, phục vụ nhanh và nhiệt tình. Giá cả rẻ, khẩu phần nhiều. Quán mở cũng khá muộn, đi mùa hè còn được ngồi điều hoà sạch sẽ. Vì mình thấy quán cũng vắng khách nên sẽ không chê, vì giá cả với đồ ăn như vậy là quá ok rồi."
    },
    {
     "name": "Hiền Thu",
     "rating": 4,
     "content": "Quán đã cải thiện khá nhiều. Lần đầu mình ăn thật sự khá khó ăn, bị ngán và xôi dính, nhưng lần này quay lại chất lượng xôi đã thay đổi nhiều, dễ ăn hơn."
    }
  ]
  },
  {
  "name": "Xôi Sùng sục - Chà Bá lửa",
  "address": "Số 1 ngõ 59 Chùa Láng (SĐT: 0264285214)",
  "distance": "350m",
  "price": "<30k",
  "type": ["Cơm/Xôi/Cháo"],
  "time": ["Sáng", "Trưa", "Tối"],
  "hours": "8:00 - 22:00",
  "menu": [
      {"dish": "Xôi ruốc hành", "price": "20k"},
      {"dish": "Xôi ruốc hành rong biển", "price": "25k"},
      {"dish": "Xôi gà xé bơ tỏi", "price": "25k"},
      {"dish": "Xôi đặc biệt trứng rán + Coca", "price": "40k"},
      {"dish": "Xôi gà nướng trứng rán + Coca", "price": "50k"},
      {"dish": "Xôi đùi gà", "price": "55k"},
      {"dish": "Xôi gà nướng tứ xuyên", "price": "45k"},
      {
        "dish": "Xôi fulltopping (đùi gà, trứng ốp, 4 lạp xưởng, ruốc, hành, giò, gà nướng tứ xuyên, 3 nem ram)",
        "price": "60k"
      }
  ],
  "reviews": [
    {
     "name": "Huyền Linh Vũ",
     "rating": 5,
     "content": "Quán rất cute, phục vụ nhanh và nhiệt tình. Giá cả rẻ, khẩu phần nhiều. Quán mở cũng khá muộn, đi mùa hè còn được ngồi điều hoà sạch sẽ. Vì mình thấy quán cũng vắng khách nên sẽ không chê, vì giá cả với đồ ăn như vậy là quá ok rồi."
    },
    {
     "name": "Hiền Thu",
     "rating": 4,
     "content": "Quán đã cải thiện khá nhiều. Lần đầu mình ăn thật sự khá khó ăn, bị ngán và xôi dính, nhưng lần này quay lại chất lượng xôi đã thay đổi nhiều, dễ ăn hơn."
    }
  ]
 },
 {
 "name": "Punnata - Cháo se nghệ nhân (Cơ sở 2)",
 "address": "66 Chùa Láng (SĐT: 0916516738)",
 "distance": "300m",
 "price": "40-50k",
 "type": ["Cơm/Xôi/Cháo"],
 "time": ["Sáng", "Trưa"],
 "hours": "",
 "menu": [
      {"dish": "Cháo se sườn sụn", "price": "35k"},
      {"dish": "Cháo se đặc biệt", "price": "55k"},
      {"dish": "Quẩy giòn", "price": "5k"},
      {"dish": "Trứng bắc thảo", "price": "15k"},
      {"dish": "Ruốc cá hồi", "price": "15k"},
      {"dish": "Ruốc tôm", "price": "15k"},
      {"dish": "Ruốc bề bề", "price": "15k"},
      {"dish": "Ruốc nấm", "price": "10k"},
      {"dish": "Ruốc heo", "price": "10k"},
      {"dish": "Thêm sườn sụn", "price": "15k"},
      {"dish": "Thịt băm", "price": "10k"}
  ],
  "reviews": [
      {
        "name": "Mầm đậu",
        "rating": 5,
        "content": "Ăn ở đây 2 lần rồi, ổn áp lắm luôn"
      },
      {
        "name": "Bảo Châu",
        "rating": 4,
        "content": "Nhiều người chê nhưng ngon mà, chất lắm ý"
      }
   ]
 },
 {
 "name": "Kim Mari Chicken",
 "address": "100 Phố Chùa Láng",
 "distance": "74m",
 "price": "120k-170k",
 "type": ["Đồ Hàn"],
 "time": ["Trưa", "Tối"],
 "hours": "10:00 - 22:30",
 "menu": [
      {"dish": "Gà rán", "price": "150k"},
      {"dish": "Gà sốt ngọt", "price": "160k"},
      {"dish": "Gà lắc phô mai", "price": "160k"},
      {"dish": "Gà sốt teriyaki", "price": "160k"},
      {"dish": "Gà sốt rau mùi", "price": "170k"},
      {"dish": "Gà sốt kim chi", "price": "170k"},
      {"dish": "Gà sốt kem hành", "price": "170k"},
      {"dish": "Gà King Triple", "price": "170k"},
      {"dish": "Tokbokki", "price": "120k"},
      {"dish": "Rose tokbokki", "price": "130k"},
      {"dish": "Mỳ ý rose", "price": "140k"},
      {"dish": "Mì ý cay", "price": "130k"},
      {"dish": "Mì tương đen", "price": "140k"},
      {"dish": "Mì trộn dầu tía tô", "price": "130k"},
      {"dish": "Mì lạnh sợi nhỏ", "price": "140k"},
      {"dish": "Mỳ udon chả cá", "price": "125k"},
      {"dish": "Canh bí ngòi cay", "price": "130k"},
      {"dish": "Thịt chiên xù", "price": "130k"}
  ],
  "reviews": [
      {
      "name": "the zionx.x_x",
      "rating": 4,
      "content": "Đồ ăn như gà, khoai tây, cheese ball đều khá ổn. Gà giòn, cheese ball béo ngậy, dai dai, canh kim chi ngon. Đi nhóm đông gọi combo rất no, còn dư mang về. Sốt chấm ở mức ổn, có một loại sốt béo khá giống sốt kebab. Mì và thịt nguội không ấn tượng. Nhân viên chăm sóc khách tốt, không gian rộng rãi, tầng trên ngồi khá chill."
      },
      {
      "name": "Yến Linh Nguyễn",
      "rating": 4,
      "content": "Quán to đẹp, giá hợp lí. Đi 2 người gọi 2 món là no, khoảng 130-150k/người. Gà lắc phô mai ngon, nóng, miếng to, thịt juicy, da giòn nhưng hơi mùi dầu. Nhân viên nhanh nhẹn, tổng thể trải nghiệm 8,5/10."
      }
  ]
},
{
"name": "Nhà Hàng OnJeong (온정)",
"address": "32 Phố Chùa Láng, Đống Đa",
"distance": "350m",
"price": ">50k",
"type": ["Đồ Hàn"],
"time": ["Trưa", "Tối"],
"hours": "9:00 - 22:00",
"menu": [
      {"dish": "Tokbokki rose", "price": "89k (Size L: 178k)"},
      {"dish": "Tokbokki Basil cream", "price": "89k (Size L: 178k)"},
      {"dish": "Gà chiên", "price": "179k (nửa con) - 358k (nguyên con)"},
      {"dish": "Gà chiên xốt", "price": "210k (nửa con) - 420k (nguyên con)"},
      {"dish": "Set gà viên chiên xốt + khoai lang chips + khoai tây chiên", "price": "120k"},
      {"dish": "Canh kimchi", "price": "80k"},
      {"dish": "Canh chả cá", "price": "60k"},
      {"dish": "Canh gà tần sâm", "price": "150k"},
      {"dish": "Bò xào bulgogi", "price": "350k"},
      {"dish": "Mì OnJeong", "price": "55k"},
      {"dish": "Mì lạnh nước", "price": "95k"},
      {"dish": "Mỳ lạnh trộn", "price": "99k"},
      {"dish": "Mỳ tương đen", "price": "120k"},
      {"dish": "Miến trộn cung đình", "price": "90k"},
      {"dish": "Lẩu quân đội", "price": "169k"},
      {"dish": "Lẩu tokbokki (2 người)", "price": "130k"},
      {"dish": "Lẩu Shabu Shabu", "price": "350k (M) - 490k (L)"},
      {"dish": "Cơm mực xào", "price": "79k"},
      {"dish": "Cơm rang kimchi", "price": "75k"},
      {"dish": "Cơm gà Mayo", "price": "75k"},
      {"dish": "Cơm/Mì gà xào cay", "price": "129k"},
      {"dish": "Set thịt chiên xù", "price": "120k"},
      {"dish": "Set thịt chiên xù phô mai", "price": "150k"}
  ],
  "reviews": [
      {
      "name": "Nguyên Đỗ",
      "rating": 4,
      "content": "Quán to, xinh, tông trắng sạch sẽ, bàn ghế rộng ngồi thoải mái. Menu đa dạng, có suất nhỏ và to. Đồ ăn ở mức ổn, gà và tok hơi ngọt, set chiên ít hơn hình. Nhân viên phục vụ ổn, quán sạch sẽ, phù hợp đi nhóm bạn."
      },
      {
      "name": "Tung Dao",
      "rating": 4,
      "content": "Chất lượng đồ ăn ổn, gà rán và tok khá ấn tượng. Giá hợp lý tầm 150-200k/người, nhân viên phục vụ tốt, không gian sạch sẽ mát mẻ. Nhìn chung khá ưng và sẽ quay lại."
      }
  ]
},
{
"name": "K-Pub Chicken",
"address": "4 Ngõ 121 Chùa Láng",
"distance": "350m",
"price": ">50k",
"type": ["Đồ Hàn"],
"time": ["Trưa", "Tối"],
"hours": "9:00 - 22:00",
"menu": [
      {"dish": "Gà sốt kem hành", "price": "149k (Không xương) - 139k (Cả xương)"},
      {"dish": "Gà sốt chua ngọt", "price": "149k (Không xương) - 139k (Cả xương)"},
      {"dish": "Gà sốt phô mai", "price": "149k (Không xương) - 139k (Cả xương)"},
      {"dish": "Gà nguyên vị", "price": "139k (Không xương) - 129k (Cả xương)"},
      {"dish": "Gà xào cay (Phần nhỏ)", "price": "59k"},
      {"dish": "Gà xào cay phô mai (Phần nhỏ)", "price": "69k"},
      {"dish": "K-Pub - Kimbap", "price": "42k"},
      {"dish": "Kimbap bò", "price": "49k"},
      {"dish": "Tokbokki", "price": "49k"},
      {"dish": "Canh chả cá", "price": "49k"},
      {"dish": "Mỳ cay", "price": "42k"},
      {"dish": "Mỳ tương đen", "price": "45k"},
      {"dish": "Mỳ spaghetti sốt kem nấm", "price": "75k"}
],
"reviews": [
      {
      "name": "Ho Song",
      "rating": 2,
      "content": "Gà cốc 49k phần rất ít, miếng gà nhỏ, sốt không đặc biệt, gà hơi chua. Nhân viên nhiệt tình nhưng đồ ăn không tương xứng với giá."
      },
      {
      "name": "Hoàng Nguyễn Việt",
      "rating": 1,
      "content": "Trải nghiệm khá tệ: vỏ gà nhão, tokbokki loãng, phục vụ nước chậm. Giá trên web và lúc thanh toán không khớp, cảm giác không xứng đáng với số tiền bỏ ra."
      }
   ]
},
{
"name": "Maru Korean Food & Dessert",
"address": "980 Đường Láng",
"distance": "750m",
"price": ">50k",
"type": ["Đồ Hàn"],
"time": ["Trưa", "Tối"],
"hours": "9:00 - 22:00",
"menu": [
      {"dish": "Set nướng đặc biệt 2", "price": "259k"},
      {"dish": "Combo Maru nướng", "price": "295k"},
      {"dish": "Set thịt nướng Maru meat lover", "price": "289k"},
      {"dish": "Combo gà mix", "price": "340k"},
      {"dish": "Combo spring", "price": "439k"},
      {"dish": "Lẩu Tokbokki redflag 2 vị", "price": "369k"},
      {"dish": "Lẩu xào bắp cải phô mai", "price": "215k"},
      {"dish": "Cơm trộn bò bulgogi", "price": "69k"},
      {"dish": "Canh chả cá Hàn Quốc", "price": "69k"},
      {
      "dish": "Maru couple 1 (Gimbab thịt + Miến trộn + Gà viên phô mai + Salad rong biển + Mandu)",
      "price": "189k"
      }
  ],
"reviews": [
      {
      "name": "Marilyn Đào",
      "rating": 4,
      "content": "Không gian rộng rãi, panchan và salad ngon. Recommend gà sốt và các loại thịt nướng. Đồ chiên và tok ở mức ổn, canh rong biển khá ổ"
      }
  ]
},
{
"name": "San Tokbokki Chùa Láng",
"address": "46 Ngõ 59 Chùa Láng, Đống Đa",
"distance": "350m",
"price": "30-40k",
"type": ["Đồ Hàn"],
"time": ["Sáng", "Trưa"],
"hours": "10:00 - 22:15",
"menu": [
      {"dish": "Original Tokbokki", "price": "11k"},
      {"dish": "Cheese tokbokki", "price": "16k"},
      {"dish": "Gà cay", "price": "21k"},
      {"dish": "Chả cá", "price": "11k"},
      {"dish": "Cơm thịt chiên xù", "price": "36k"},
      {"dish": "Cơm thịt chiên phô mai", "price": "46k"},
      {"dish": "Cơm trộn Hàn Quốc", "price": "36k"},
      {"dish": "Cơm bít tết trứng", "price": "41k"},
      {"dish": "Cơm gà sốt cay", "price": "36k"},
      {"dish": "Mỳ đen", "price": "36k"},
      {"dish": "Mỳ cay", "price": "36k"},
      {"dish": "Mỳ udon", "price": "36k"},
      {"dish": "Thịt ba chỉ chiên", "price": "21k"},
      {"dish": "Kimbap đồng giá", "price": "16k"}
  ],
"reviews": [
      {
      "name": "Hân Ngọc",
      "rating": 3,
      "content": "Đồ ăn ổn so với tầm giá, giá rẻ nên không đòi hỏi nhiều, muốn ăn ngon hơn thì sẽ chọn quán khác."
      },
      {
      "name": "Ngọc Anh Dương",
      "rating": 4,
      "content": "Quán đúng chuẩn dành cho sinh viên với mức giá rất hợp lí. Cơm thịt chiên xù 36k, thịt giòn mềm. Tokbokki và kimbap rất rẻ, món ra nhanh, gọi món bằng quét mã. Đồ ăn không quá xuất sắc nhưng ổn trong tầm giá."
      }
  ]
},
{
"name": "Huy Go cook",
"address": "130 Phố Chùa Láng",
"distance": "600m",
"price": ">50k",
"type": ["Đồ Hàn"],
"time": ["Trưa", "Tối"],
"hours": "10:00 - 14:00, 17:00 - 22:00",
"menu": [
      {"dish": "Mỳ tương đen", "price": "75k"},
      {"dish": "Mỳ trộn chả cá phô mai sốt rose", "price": "90k"},
      {"dish": "Miến trộn Hàn Quốc", "price": "75k"},
      {"dish": "Canh Kimchi hầm", "price": "50k"},
      {"dish": "Mỳ kim chi phô mai bacon", "price": "75k"},
      {"dish": "Mỳ trộn trứng lòng đào", "price": "60k"},
      {"dish": "Tokbokki chả cá", "price": "65k"},
      {"dish": "Rose Tokbokki", "price": "90k"},
      {"dish": "Kimbap xúc xích phô mai", "price": "50k"},
      {"dish": "Kimbap lườn ngỗng hun khói", "price": "65k"},
      {"dish": "Cơm nắm rong biển phô mai", "price": "55k"},
      {"dish": "Cơm thịt heo sốt cay trứng lòng đào", "price": "69k"},
      {"dish": "Cơm trộn sốt cay/chua ngọt", "price": "69k"},
      {"dish": "Gà rán truyền thống", "price": "60k"},
      {"dish": "Gà rán lắc phô mai", "price": "65k"},
      {"dish": "Gà rán sốt mù tạt mật ong", "price": "69k"},
      {"dish": "Lẩu tokbokki quân đội", "price": "269k"}
  ],
"reviews": [
      {
      "name": "Thanh Hoài",
      "rating": 4,
      "content": "Đồ ăn ngon, gà nêm nếm vừa miệng, món ăn kèm ổn không bị ngán. Không gian hơi xanh, ánh sáng chưa hợp chụp hình. Giờ cao điểm chỗ để xe hơi ít, nhìn chung là quán ăn ngon, phù hợp đi ăn nhẹ hoặc tụ tập bạn bè."
      },
      {
      "name": "Amo",
      "rating": 5,
      "content": "Lần đầu ăn ở quán, gọi set 255k hợp cho 1-2 người. Mì kimchi phô mai bacon rất ngon, gà giòn sốt chua ngọt đậm vị. Quán sạch sẽ, nhân viên nhiệt tình dắt xe. Sẽ quay lại và giới thiệu bạn bè."
      }
  ]
},
{
"name": "Mukbang - Đồ ăn Hàn Quốc",
"address": "141 Phố Chùa Láng",
"distance": "350m",
"price": ">50k",
"type": ["Đồ Hàn"],
"time": ["Trưa", "Tối"],
"hours": "Mở cả ngày",
"menu": [
      {"dish": "Salad lườn ngỗng sốt mè rang", "price": "75k"},
      {"dish": "Cơm trộn truyền thống trứng ốp", "price": "69k"},
      {"dish": "Cơm gà sốt nướng phô mai", "price": "89k"},
      {"dish": "Kimbap gà cajun sốt teriyaki", "price": "85k"},
      {"dish": "Kimbap chiên ruốc cay", "price": "65k"},
      {"dish": "Cơm chiên kimchi trứng lốc xoáy", "price": "85k"},
      {"dish": "Cơm thịt chiên xù sốt cari", "price": "69k"},
      {"dish": "Tokbokki phô mai sốt rose", "price": "89k"},
      {"dish": "Mỳ tương đen", "price": "75k"},
      {"dish": "Mỳ lạnh bò bulgogi", "price": "109k"},
      {"dish": "Miến trộn truyền thống", "price": "75k"},
      {"dish": "Udon xào bò bulgogi", "price": "85k"},
      {"dish": "Gà viên sốt ngọt/cay", "price": "59k"},
      {"dish": "Gà viên sốt kem hành", "price": "75k"}
  ],
"reviews": [
      {
      "name": "Hiền Bùi",
      "rating": 3,
      "content": "Gà xào cay ngon, panchan cho nhiều nhưng quầy line buffet nguội, đợi khoảng 10 phút."
      },
      {
      "name": "Linh Nguyễn",
      "rating": 3,
      "content": "Đồ ăn mức trung bình phù hợp giá sinh viên, nên gọi set cho tiết kiệm. Món nhiều nhưng nêm nếm chưa tới, panchan nhiều nhưng không ngon. Không gian có dấu hiệu xuống cấp, bù lại nhân viên phục vụ nhanh và nhiệt tình."
      }
  ]
},
{
"name": "Hola Tacos",
"address": "143 Phố Chùa Láng",
"distance": "350m",
"price": "30-40k",
"type": ["Tacos"],
"time": ["Sáng", "Trưa"],
"hours": "Mở cả ngày",
"menu": [
      {"dish": "Bò bằm", "price": "19k (S)"},
      {"dish": "Gà nướng BBQ", "price": "18k (S)"},
      {"dish": "Trứng xúc xích truyền thống", "price": "25k"},
      {"dish": "Gà giòn bơ cay Mexico", "price": "30k"},
      {"dish": "Bò bằm đậm vị sốt", "price": "30k"},
      {"dish": "Gà BBQ bơ phô mai", "price": "30k"},
      {"dish": "Bò nướng BBQ Hàn Quốc", "price": "35k"},
      {"dish": "Tôm chiên giòn phủ sốt", "price": "35k"},
      {"dish": "Đặc biệt mix vị gà giòn xúc xích", "price": "35k"},
      {"dish": "Hamburger bò bằm đậm vị sốt", "price": "25k"},
      {"dish": "Hamburger gà giòn Hàn Quốc", "price": "30k"},
      {"dish": "Hamburger tôm chiên giòn phủ sốt", "price": "35k"}
  ],
"reviews": [
      {
      "name": "Ngan nguyen",
      "rating": 5,
      "content": "Xốt không quá đa dạng nhưng nhân bò, gà rất ngon và chất lượng, thịt tươi, hợp khẩu vị người Việt. Trẻ con cũng thích ăn, kể cả rau. Món ăn cải tiến tốt, nguyên liệu nhìn rất tươi."
      },
      {
      "name": "Phình má phun lửa",
      "rating": 3,
      "content": "Bánh bò bằm đậm vị ăn khá ổn, thịt ngon, sốt hài hoà, không ngấy. Tuy nhiên nhược điểm lớn là nhân bò nhiều dầu, bánh bị thấm dầu làm mềm vỏ và khá bẩn khi ăn. Nếu khắc phục được điểm này thì hương vị và giá đều ổn."
      }
  ]
},
{
"name": "Tacos Măm",
"address": "27 Chùa Láng - 116 Chùa Láng",
"distance": "350m",
"price": "30-40k",
"type": ["Tacos"],
"time": ["Sáng", "Trưa"],
"hours": "7:30 - 21:45",
"menu": [
      {"dish": "Tacos Bò", "price": "45k"},
      {"dish": "Tacos Gà", "price": "39k"},
      {"dish": "Tacos xúc xích hun khói", "price": "35k"}
  ],
"reviews": [
      {
      "name": "Thu Trang Nguyễn",
      "rating": 4,
      "content": "Ăn thử bánh nhân bò xay, nhân khá đầy đặn so với mức giá. Sốt ngon, sẽ quay lại."
      }
  ]
},
{
"name": "Bún cá cô Tuyết",
"address": "Số 24 Ngõ 84 Chùa Láng",
"distance": "210m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "5:30 - 21:30",
"menu": [
      { "dish": "Bún cá 1 topping", "price": "30k" },
      { "dish": "Bún cá 2 topping", "price": "35k" },
      { "dish": "Bún cá 3 topping", "price": "40k" },
      { "dish": "Bún cá đặc biệt", "price": "45k" }
  ],
"reviews": [
      {
      "name": "Võ Hoàng",
      "rating": 5,
      "content": "Quán ngon 10 điểm, giá sinh viên, sạch hơn ngoài chợ 84"
      }
  ]
},
{
"name": "Súp cua GA",
"address": "Số 6A Ngõ 91 Chùa Láng",
"distance": "140m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "8:00 - 22:00",
"menu": [
      { "dish": "Súp gà", "price": "30k" },
      { "dish": "Súp cua", "price": "35k" },
      { "dish": "Súp tôm", "price": "50k" },
      { "dish": "Súp sò điệp", "price": "50k" },
      { "dish": "Súp hải sản đặc biệt", "price": "60k" },
      { "dish": "Ngô xào trứng muối", "price": "33k" },
      { "dish": "Bánh canh chả cá", "price": "35k" },
      { "dish": "Bánh canh chả tôm", "price": "40k" },
      { "dish": "Bánh canh sườn tôm", "price": "50k" },
      { "dish": "Bánh canh thập cẩm", "price": "60k" },
      { "dish": "Bánh canh đặc biệt", "price": "75k" }
  ],
"reviews": [
      {
      "name": "the zionx.x_x",
      "rating": 3,
      "content": "Súp cua ngon, nhưng cách làm việc của quán khiến khách thấy khó chịu"
      },
      {
      "name": "Tran Tran",
      "rating": 5,
      "content": "Súp cua ngon bát đầy, quán rộng rãi có 2 tầng, trà đá đầy đủ, có điều hòa thoáng mát, giá rẻ hợp khẩu vị, nhân viên phục vụ nhanh chóng"
      },
      {
      "name": "Tiểu Ly",
      "rating": 5,
      "content": "Mình gọi 1 súp cua thêm trứng bắc thảo và óc heo, ăn khá ngon"
      }
  ]
},
{
"name": "Bún đậu Chùa Láng",
"address": "Số 33 Ngõ 185 Chùa Láng",
"distance": "650m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "9:00 - 20:30",
"menu": [
      { "dish": "Bún đậu", "price": "25k" },
      { "dish": "Đầy đủ nhỏ", "price": "35k" },
      { "dish": "Đầy đủ to", "price": "40k" },
      { "dish": "Đặc biệt", "price": "50k" }
  ],
"reviews": [
      {
      "name": "TRÂM ANH NGUYỄN NGỌC",
      "rating": 5,
      "content": "Bún đậu ngon, đầy đặn"
      },
      {
      "name": "Hoa Le",
      "rating": 3,
      "content": "Topping ăn ổn áp, đầy đủ và chất lượng ổn, tuy nhiên mắm tôm và nước mắm chưa thực sự ngon nên chưa làm bật vị món ăn"
      },
      {
      "name": "Khánh Ngọc",
      "rating": 5,
      "content": "Bún đậu ngon nha, có dưa chuột ăn kèm nữa, vị vừa vặn, đậu giòn tan"
      }
  ]
},
{
"name": "Bún đỏ Chùa Láng",
"address": "Số 6 Ngõ 185 Chùa Láng",
"distance": "500m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "10:00 - 22:00",
"menu": [
      { "dish": "Bún đỏ bát lớn", "price": "35k" },
      { "dish": "Bún đỏ bát đặc biệt", "price": "45k" }
  ],
"reviews": [
      {
      "name": "Viet Huong Nguyen",
      "rating": 4,
      "content": "Một món bún khá độc đáo ít bán ở Hà Nội, cá nhân mình thấy ăn ổn nhưng nước dùng không có gì quá đặc biệt, được cái topping rất nhiều loại và đầy đặn, gồm giò, riêu miếng, tóp mỡ, trứng, rau,..."
      },
      {
      "name": "Hieu-Tran Trung",
      "rating": 4,
      "content": "Gạch tôm độn thịt khá hay, giò tai hơi mỏng, xá xíu gần giống trong vằn thắn nhưng không ngon bằng, bún đỏ sợi to như bún bò Huế chứ vị thì không thấy khác gì, tổng thể ok, không ăn được tôm thì k nên thử"
      },
      {
      "name": "Bình Trần",
      "rating": 5,
      "content": "Trưa nay qua ăn cùng mẹ, quán làm ngon, ăn bát 35 mà mình thấy no căng, nước dùng ngọt xương, đồ ăn đủ đồ có cả quẩy ăn kèm"
      }
  ]
}, 
{
"name": "Bún bò Huế Hương Giang",
"address": "Số 42 Ngõ 185 Chùa Láng",
"distance": "650m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "8:00 - 22:00",
"menu": [
      { "dish": "Bún bò Huế không móng", "price": "30k" },
      { "dish": "Bún bò đầy đủ", "price": "35k" },
      { "dish": "Bún bò đặc biệt", "price": "40-50k" }
  ],
"reviews": [
      {
      "name": "Vũ Thị Quỳnh Trang",
      "rating": 4,
      "content": "Quán bún bò quen ở Láng, giá thành bình dân, ăn ổn, lượng khách đông nên vệ sinh dọn dẹp chưa kĩ, rau cũng không được tươi"
      },
      {
      "name": "204 nieu",
      "rating": 5,
      "content": "Đồ ăn ngon, mình ăn suất 35k mà nhiều lắm, no quá, ăn xong bún mà vẫn còn topping"
      },
      {
      "name": "Khanh Do",
      "rating": 5,
      "content": "Quán nhỏ hẹp, tầm 8 chỗ, đồ ăn làm cẩn thận và có tâm, không làm công nghiệp, ngon so với nhiều quán khác"
      }
  ]
},
{
"name": "Hi - Tôm bún hải sản",
"address": "Số 211 Chùa Láng",
"distance": "500m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "9:00 - 22:00",
"menu": [
      { "dish": "Bún chả cá", "price": "30k" },
      { "dish": "Bún hải sản đầy đủ", "price": "45k" },
      { "dish": "Bún hải sản đặc biệt", "price": "65k" }
  ],
"reviews": [
      {
      "name": "Vũ Diễm Quỳnh",
      "rating": 5,
      "content": "Bún siêu ngon, nước dùng thanh, topping tươi, có nước chấm ớt xanh"
      },
      {
      "name": "Khánh Linh Mai",
      "rating": 5,
      "content": "Bún ngon, chua cay đậm vị, được free trà hồng sâm lấy bao nhiêu cũng được, giá cả phải chăng"
      },
      {
      "name": "Trang Pham",
      "rating": 5,
      "content": "Siêu ngon, nước dùng chua cay, hải sản tươi, được free trà hồng sâm"
      }
  ]
},
{
"name": "Bún cá rô đồng",
"address": "Số 127 Chùa Láng",
"distance": "150m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "7:00 - 14:00 / 18:00 - 20:00",
"menu": [
      { "dish": "Bún hải sản", "price": "30k" }
  ],
"reviews": []
},
{
"name": "Bánh canh ghẹ 1",
"address": "Số 6A Ngách 2 Ngõ 121 Chùa Láng",
"distance": "180m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "9:00 - 20:00",
"menu": [
      { "dish": "Bánh canh ghẹ", "price": "40k" },
      { "dish": "Bún bò Huế", "price": "30k" },
      { "dish": "Bánh các loại (suất nhỏ)", "price": "30k" }
  ],
"reviews": []
},
{
"name": "Bánh canh ghẹ 2",
"address": "Số 4 Ngõ 91 Chùa Láng",
"distance": "140m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "8:30 - 19:30",
"menu": [
      { "dish": "Bánh canh ghẹ", "price": "35k" },
      { "dish": "Bún Thái hải sản", "price": "40k" },
      { "dish": "Cơm gà cà ri", "price": "45k" },
      { "dish": "Bánh mì cà ri", "price": "45k" }
  ],
"reviews": [
      {
      "name": "My Nguyễn",
      "rating": 3,
      "content": "Bánh canh ngon, quán sạch sẽ, bác gái tóc xoăn phục vụ rất khó chịu"
      },
      {
      "name": "Quỳnh Chi",
      "rating": 5,
      "content": "Vị thì hơi khác so với lần mình ăn trong Nam, chắc là đậm đà hơn á, một phần ăn là no nha"
      },
      {
      "name": "Nguyễn Phi",
      "rating": 5,
      "content": "Ăn vừa miệng, bánh canh cũng khá khác, sợi to hơn và dài hơn"
      }
  ]
},
{
"name": "Bún bò Huế O - Nga",
"address": "Số 181 Chùa Láng",
"distance": "500m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "6:30 - 22:00",
"menu": [
      { "dish": "Bún bò Huế tô trẻ em", "price": "30k" },
      { "dish": "Bún bò Huế tô trắng", "price": "40k" },
      { "dish": "Bún bò Huế tô xanh", "price": "50k" },
      { "dish": "Bún bò Huế tô đen", "price": "60k" }
   ],
"reviews": [
      {
      "name": "Dương Quang Trung",
      "rating": 4,
      "content": "Quán hơi tối, có cách phân chia menu theo màu bát khá đặc biệt"
      },
      {
      "name": "Hoài",
      "rating": 5,
      "content": "Ngon, no căng bụng"
      }
  ]
},
{
"name": "Bánh canh ghẹ",
"address": "Số 2 Ngõ 121 Chùa Láng",
"distance": "180m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "",
"menu": [
      { "dish": "Bánh canh ghẹ bột lọc", "price": "50k" },
      { "dish": "Bún bò Huế", "price": "" },
      { "dish": "Bánh bột lọc", "price": "" }
  ],
"reviews": [
      {
      "name": "Hai Thanh Tran",
      "rating": 5,
      "content": "Sợi bánh bột lọc rất ngon"
      }
  ]
},
{
"name": "Bún bò Huế O Chang - Bún bò Nam Bộ",
"address": "Số 79 Chùa Láng",
"distance": "20m",
"price": ">50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "7:00 - 22:00",
"menu": [
      { "dish": "Bún bò Huế", "price": "45k" },
      { "dish": "Bún bò Huế đặc biệt", "price": "55k" },
      { "dish": "Bún bò Huế chả cua", "price": "65k" },
      { "dish": "Bún đuôi bò / gân bò", "price": "60k" },
      { "dish": "Bún bò trộn Nam Bộ", "price": "50-60k" },
      { "dish": "Lẩu đuôi bò", "price": "350k - 450k - 550k" },
      { "dish": "Cơm rang thập cẩm / Cơm rang dưa bò", "price": "45-55k" }
  ],
"reviews": [
      {
      "name": "Anh Hà Huyền",
      "rating": 5,
      "content": "Quán sạch sẽ, nước dùng đậm vị, ai thích ăn nhanh có thể cân nhắc"
      },
      {
      "name": "Tuấn Hùng Hoàng",
      "rating": 5,
      "content": "Bún bò Huế và bún trộn đều ở mức khá trở lên, thịt bò dai mềm ngọt, tiết không hôi, đồ ăn kèm sạch sẽ và đầy đủ"
      }
  ]
},
{
"name": "Bún riêu cua tóp mỡ Huỳnh Anh",
"address": "Số 114 Chùa Láng",
"distance": "450m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "",
"menu": [
      { "dish": "Bún riêu cua đậu", "price": "30k" },
      { "dish": "Bún riêu cua bò/giò", "price": "40k" },
      { "dish": "Bún riêu cua bò tóp mỡ", "price": "45k" },
      { "dish": "Bún riêu cua bò giò tóp mỡ", "price": "50k" },
      { "dish": "Bún riêu cua tóp mỡ đầy đủ", "price": "55k" },
      { "dish": "Bún riêu cua tóp mỡ đặc biệt", "price": "65k" }
  ],
"reviews": [
      {
      "name": "Vũ Đình Hoan",
      "rating": 5,
      "content": "Đồ ăn ngon, sẽ quay lại lần nữa"
      },
      {
      "name": "Quyên Phạm",
      "rating": 1,
      "content": "Sợi bún chua, quán vệ sinh bẩn"
      }
  ]
},
{
"name": "Mì trộn Nam Béo",
"address": "Số 20 Ngõ 91 Chùa Láng",
"distance": "210m",
"price": "30-40k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "10:30 - 14:00 / 17:00 - 22:00",
"menu": [
      { "dish": "Mì trộn thường", "price": "35k" },
      { "dish": "Mì trộn đặc biệt", "price": "45k" },
      { "dish": "Mì trộn thập cẩm", "price": "55k" }
  ],
"reviews": []
},
{
"name": "Hủ tiếu",
"address": "Ngõ 91 Chùa Láng",
"distance": "70m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "",
"menu": [],
"reviews": []
},
{
"name": "Quán cô Hương Béo",
"address": "Số 61 Chùa Láng",
"distance": "150m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "Mở cửa suốt ngày đêm",
"menu": [
      { "dish": "Tô ngon miệng", "price": "40k" },
      { "dish": "Tô đầy đủ", "price": "55k" },
      { "dish": "Lẩu riêu tóp mỡ mọc giòn tươi (nhỏ)", "price": "300k" }
  ],
"reviews": [
      {
      "name": "Simon HWoon",
      "rating": 3,
      "content": "Đồ ăn bình thường, khẩu phần khá ít so với giá"
      },
      {
      "name": "Minh Minh",
      "rating": 1,
      "content": "Giá thì không rẻ nhưng đồ ăn không chất lượng"
      }
  ]
},
{
"name": "Bún cá cay Hải Phòng",
"address": "Số 128 Đường Nguyễn Chí Thanh",
"distance": "1.3km",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "6:00 - 22:00",
"menu": [
      { "dish": "Bát 35", "price": "35k" },
      { "dish": "Bát 45", "price": "45k" },
      { "dish": "Bát đặc biệt", "price": "60k" }
  ],
"reviews": [
      {
      "name": "DLA",
      "rating": 3,
      "content": "Phục vụ nhanh còn đồ ăn bình thường, hơi ít cá, vị nước dùng cũng chưa ngon lắm"
      },
      {
      "name": "Dung Lê",
      "rating": 5,
      "content": "Phục vụ nhanh, đồ ăn đa dạng, nhiều topping, nêm nếm rất vừa, hợp khẩu vị mình"
      }
  ]
},
{
"name": "Mỳ chua cay 6 phụ nữ",
"address": "Số 10 Ngách 4 Ngõ 91 Chùa Láng",
"distance": "500m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "8:00 - 21:00",
"menu": [
      { "dish": "Bún/mì chua cay bò", "price": "35k" },
      { "dish": "Bún/mì chua cay tim cật, bò", "price": "45k" },
      { "dish": "Bún/mì chua cay hải sản, tim cật", "price": "55k" },
      { "dish": "Bún/mì chua cay thập cẩm", "price": "65k" },
      { "dish": "Mỳ trộn tim cật/bò", "price": "40k" },
      { "dish": "Bún bò trộn Nam Bộ", "price": "40k" },
      { "dish": "Mì gà tần", "price": "40k" },
      { "dish": "Cơm rang Dương Châu", "price": "35k" },
      { "dish": "Trứng rán ngải cứu", "price": "20k" },
      { "dish": "Chân gà luộc", "price": "15k" }
  ],
"reviews": [
      {
      "name": "Nguyễn Khánh Linh",
      "rating": 5,
      "content": "Tổng thể thì mình thấy tạm ổn, chỗ ngồi khá sạch sẽ, quán rất đông sinh viên FTU. Món ăn ở mức ổn, phù hợp đổi vị bữa trưa"
      },
      {
      "name": "Anh Huyền",
      "rating": 1,
      "content": "3 bát mì phải đợi gần 20 phút mới ra, đồ ăn chỉ cho mì trần chan nước, lên món rất chậm"
      }
  ]
},
{
"name": "Phở gà phố cổ Bảo Lộc",
"address": "Số 35 Chùa Láng",
"distance": "170m",
"price": "40-50k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "6:00 - 23:00",
"menu": [
      { "dish": "Phở lườn/mọc", "price": "40k" },
      { "dish": "Phở đùi", "price": "50k" },
      { "dish": "Phở đặc biệt", "price": "70k" },
      { "dish": "Mỳ trộn đùi chiên mắm tỏi", "price": "60k" },
      { "dish": "Bún thang lườn", "price": "55k" },
      { "dish": "Cơm đùi chiên", "price": "55k" },
      { "dish": "Cháo lườn xé", "price": "35k" }
  ],
"reviews": [
      {
      "name": "Tran Pham",
      "rating": 4,
      "content": "Quán ngon, giá hợp lý, đồ ăn ổn, quán sạch sẽ, nhân viên phục vụ ổn"
      },
      {
      "name": "diep diep",
      "rating": 1,
      "content": "Cơm chỉ ở mức tạm, quán nên training lại nhân viên"
      }
  ]
},
{
"name": "Bún riêu Dung MaMa - Chùa Láng",
"address": "Số 41 Chùa Láng",
"distance": "170m",
"price": "<30k",
"type": ["Bún/Phở/Miến/Bánh canh/Súp"],
"time": ["Sáng", "Trưa", "Tối"],
"hours": "6:30 - 21:30",
"menu": [
      { "dish": "Bát cơ bản", "price": "25k" }
  ],
"reviews": [
      {
      "name": "Minh Trần",
      "rating": 5,
      "content": "Đồ ăn ngon, không gian sạch sẽ, phục vụ tận tình"
      },
      {
      "name": "Ngọc Anh Lê",
      "rating": 5,
      "content": "Bún ngon nha, thơm vị giấm bỗng và có vị tanh của riêu, giống kiểu vị bún riêu xưa mình từng ăn"
      },
      {
      "name": "Hiu Hwang",
      "rating": 3,
      "content": "Không có gì đặc sắc, bàn ghế hơi thấp, giá cả trung bình, bún và bánh đa không có gì nổi bật cả"
      }
  ]
},
  {
    "name": "Nem nướng Nha Trang Anh Tư Béo",
    "address": "Số 151 Chùa Láng",
    "distance": "220m",
    "price": "30-40k",
    "type": ["Nem nướng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "9:00 - 22:00",
    "menu": [
      { "dish": "Nem nướng", "price": "35k" },
      { "dish": "Nem nướng vip", "price": "55k" },
      { "dish": "Bánh bột lọc (1 suất/6 cái)", "price": "35k" },
      { "dish": "Nem chua rán", "price": "35k" },
      { "dish": "Chân gà sốt Thái", "price": "40k" }
    ],
    "reviews": [
      {
        "name": "Đặng Thúy Quỳnh",
        "rating": 5,
        "content": "Quán nem nướng Nha Trang tủ của mình, 10đ không nói nhiều"
      },
      {
        "name": "Mai Lan Hoàng",
        "rating": 5,
        "content": "Cô chú rất nhiệt tình, ăn ngon, quán sạch sẽ thoáng mát, mình ăn rất nhiều lần rồi"
      },
      {
        "name": "Hà Hoàng",
        "rating": 5,
        "content": "Nem nướng bình thường, không đặc sắc lắm, nước chấm cũng tạm, nem chua rán không ngon lắm"
      }
    ]
  },
  {
    "name": "Nem nướng Nha Trang Vân Linh",
    "address": "Số 18 Ngõ 59 Chùa Láng",
    "distance": "230m",
    "price": "30-40k",
    "type": ["Nem nướng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "",
    "menu": [
      { "dish": "Nem nướng Nha Trang", "price": "35k" },
      { "dish": "Thịt nem nướng", "price": "18k" }
    ],
    "reviews": [
      {
        "name": "Nguyệt Nguyễn Minh",
        "rating": 5,
        "content": "1 suất siêu đầy đặn siêu nhiều! Quán sạch sẽ, ăn xong no căng luôn, nước chấm vừa miệng"
      },
      {
        "name": "Lê Hà Linh",
        "rating": 5,
        "content": "Quán sạch sẽ, đi tầm 11h trưa sẽ vắng và thoáng mát, đồ ăn ở mức ổn trong tầm giá"
      },
      {
        "name": "Uyên Mai",
        "rating": 5,
        "content": "Một suất 2 người ăn rất nhiều rau và nem, ăn no lắm luôn, 10 sao nha"
      }
    ]
  },
  {
    "name": "Nem nướng Nha Trang Tâm Việt",
    "address": "Số 10 Ngõ 121 Chùa Láng",
    "distance": "240m",
    "price": "40-50k",
    "type": ["Nem nướng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "9:00 - 14:00 / 15:00 - 21:00",
    "menu": [
      { "dish": "Nem nướng Nha Trang", "price": "39k" },
      { "dish": "Thịt nem nướng", "price": "18k" },
      { "dish": "Bún chả cá Nha Trang", "price": "40k" },
      { "dish": "Bánh tráng cuốn thịt heo luộc", "price": "55k" },
      { "dish": "Bánh tráng cuốn thịt heo quay", "price": "65k" }
    ],
    "reviews": [
      {
        "name": "Vân Vũ Thảo",
        "rating": 4,
        "content": "Quán đông khách nhưng mình không cần chờ, đến là có bàn"
      },
      {
        "name": "Diệp Đặng",
        "rating": 4,
        "content": "Suất nem đầy đặn, sạch sẽ, rau tươi, nem ổn nhưng chưa quá đặc sắc, nước chấm bình thường"
      },
      {
        "name": "Hà Vũ Hải",
        "rating": 5,
        "content": "Đồ ăn ok, phục vụ nhiệt tình vui vẻ, sốt chấm và rau gọi thoải mái"
      }
    ]
  },
  {
    "name": "Koifood - Buffet nem nướng Nha Trang",
    "address": "Số 122C Ngõ 1194 Đường Láng",
    "distance": "700m",
    "price": "45k - 60k",
    "type": ["Nem nướng", "Buffet"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "10:00 - 24:00",
    "menu": [
      { "dish": "Buffet nem nướng", "price": "45k" },
      { "dish": "Buffet nước", "price": "15k" }
    ],
    "reviews": []
  },
  {
    "name": "Dơm - Vua Bánh Tráng",
    "address": "Số 34 Huỳnh Thúc Kháng",
    "distance": "300m",
    "price": "30-40k",
    "type": ["Bánh tráng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "9:00 - 22:00",
    "menu": [
      { "dish": "Buffet bánh tráng", "price": "69k" },
      { "dish": "Bánh tráng cuộn bơ sốt me", "price": "27k" },
      { "dish": "Bánh tráng chấm", "price": "20k" },
      { "dish": "Bánh tráng nướng truyền thống", "price": "20k" },
      { "dish": "Bánh tráng nướng phô mai đặc biệt", "price": "45k" },
      { "dish": "Bánh tráng trộn đặc biệt", "price": "32k" }
    ],
    "reviews": [
      {
        "name": "lamkaoo",
        "rating": 3,
        "content": "Quán có thể ngồi trong nhà hoặc ngoài trời nhưng hơi khó tìm điểm đỗ xe"
      },
      {
        "name": "Isolde Andrea",
        "rating": 5,
        "content": "Quán có nhiều loại bánh tráng, bánh mềm vừa phải, gia vị đậm đà, nhiều topping như xoài, trứng cút, khô bò, hành phi"
      },
      {
        "name": "Lê Minh Tuấn Phùng",
        "rating": 4,
        "content": "Đi 2 người ăn buffet, trải nghiệm chưa tốt vì đồ lên khá chậm"
      },
      {
        "name": "Thái Ngân",
        "rating": 5,
        "content": "Lần đầu trải nghiệm rất hài lòng, đi theo review TikTok và không thất vọng"
      }
    ]
  },
  {
    "name": "Bánh tráng Nhím",
    "address": "Số 1 Ngõ 84 Chùa Láng",
    "distance": "80m",
    "price": "<30k",
    "type": ["Bánh tráng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "11:00 - 23:00",
    "menu": [
      { "dish": "Bánh tráng nướng", "price": "25k" },
      { "dish": "Bánh tráng trộn", "price": "25k" },
      { "dish": "Bánh tráng cuộn", "price": "30k" },
      { "dish": "Bánh trứng cút nướng", "price": "35k" },
      { "dish": "Ngô xào tép", "price": "30k" },
      { "dish": "Nộm xoài bò khô", "price": "30k" },
      { "dish": "Khoai tây chiên", "price": "30k" }
    ],
    "reviews": [
      {
        "name": "Quỳnh Anh Đặng",
        "rating": 5,
        "content": "Không gian sáng sủa, sạch sẽ, đồ ăn giá phải chăng và ngon vượt mong đợi"
      },
      {
        "name": "Quyen Bui",
        "rating": 5,
        "content": "Đặt qua Grab, vị đậm đà, bánh tráng cuộn ngon, trộn ổn nhưng hơi ít xoài"
      },
      {
        "name": "Mèo Ngáo",
        "rating": 4,
        "content": "Bánh tráng nướng giòn, topping nhiều, ăn khá no"
      }
    ]
  },
  {
    "name": "Tina Trần Bistro",
    "address": "Số 45 Ngõ 33 Chùa Láng",
    "distance": "290m",
    "price": "<30k",
    "type": ["Bánh tráng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "10:00 - 22:00",
    "menu": [
      { "dish": "Bánh tráng trộn thường", "price": "15k" },
      { "dish": "Bánh tráng cuộn bơ", "price": "25k" },
      { "dish": "Bánh tráng nướng trứng tép thịt", "price": "15k" },
      { "dish": "Chén trứng nướng", "price": "15k" },
      { "dish": "Trứng cút lộn xào me", "price": "25k" }
    ],
    "reviews": [
      {
        "name": "Ph Linh Ng",
        "rating": 4,
        "content": "Bánh tráng nhiều nước hơn nên hơi nhạt, bơ ngậy lạ miệng nhưng ăn nhiều hơi ngán"
      },
      {
        "name": "Kiên Hải",
        "rating": 5,
        "content": "Món ngon, chị chủ dễ thương, nên thử"
      },
      {
        "name": "Thoa Vũ",
        "rating": 3,
        "content": "Suất hơi ít so với giá, không có món đặc biệt, bánh tráng nướng hơi tanh"
      }
    ]
  },
  {
    "name": "Bánh tráng trộn Sài Gòn - Chùa Láng",
    "address": "Số 147 Ngõ 1194 Đường Láng",
    "distance": "600m",
    "price": "<30k",
    "type": ["Bánh tráng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "",
    "menu": [
      { "dish": "Bánh tráng cuốn bơ / sốt me", "price": "30k" },
      { "dish": "Bánh tráng trộn", "price": "30k" },
      { "dish": "Bánh tráng nướng", "price": "30k" },
      { "dish": "Bánh mì muối ớt", "price": "30k" },
      { "dish": "Trứng nướng khọt", "price": "30k" },
      { "dish": "Bắp xào tép", "price": "30k" },
      { "dish": "Khô heo giả bò", "price": "30k" }
    ],
    "reviews": [
      {
        "name": "Phạm Thị Mỹ Lệ",
        "rating": 5,
        "content": "Mua mang đi"
      },
      {
        "name": "Trang Vu",
        "rating": 5,
        "content": "Ăn vào bữa trưa"
      }
    ]
  },
  {
    "name": "Bánh tráng trộn Quang Đăng",
    "address": "Số 131 Chùa Láng",
    "distance": "170m",
    "price": "<30k",
    "type": ["Bánh tráng"],
    "time": ["Sáng", "Trưa", "Tối"],
    "hours": "9:00 - 23:00",
    "menu": [
      { "dish": "Bánh tráng trộn", "price": "25k" },
      { "dish": "Bánh tráng cuộn", "price": "25k" },
      { "dish": "Bánh tráng nướng", "price": "25k" },
      { "dish": "Bánh tráng trộn da heo", "price": "35k" },
      { "dish": "Bánh tráng nướng phô mai", "price": "30k" },
      { "dish": "Viên chiên thập cẩm", "price": "35k" },
      { "dish": "Da heo lắc xoài", "price": "30k" },
      { "dish": "Da heo mắm tỏi / mắm hành", "price": "50k" },
      { "dish": "Bún trộn thịt nướng", "price": "25k" }
    ],
    "reviews": [
      {
        "name": "Ngân Thu",
        "rating": 5,
        "content": "Ăn nhiều lần vì quá ngon, nhân viên dễ thương"
      },
      {
        "name": "Chi Bùi",
        "rating": 5,
        "content": "Quán ruột của mình, thường mua mang về"
      },
      {
        "name": "Kiệt Nguyễn",
        "rating": 5,
        "content": "Đồ ăn ngon, để sốt riêng nên không bị bết"
      }
    ]
  },
  {
    "name": "Tê Tê Chicken",
    "address": "Ngõ 91, Phố Chùa Láng, Láng Thượng, Đống Đa, Hà Nội, Việt Nam",
    "distance": "200-300m",
    "price": ">50k",
    "type": ["Gà/Thịt chiên"],
    "time": ["Sáng", "Trưa", "Chiều", "Tối"],
    "hours": "08:00 - 22:00",
    "menu": [
      { "dish": "Gà cốc (lắc xí muội/ sốt kem/ lắc phô mai/ sốt xì dầu mật ong/ sốt cay ngọt)", "price": "59k" },
      { "dish": "Gà rán (sốt kem hành/ rắc phô mai/ sốt bơ tỏi)", "price": "119k" },
      { "dish": "Gà rán không xương (sốt kem hành/ sốt bơ tỏi mật ong/ sốt Mayo Honey)", "price": "129k" }
    ],
    "reviews": [
      { "name": "Tiểu Ly", "rating": 4, "content": "Đồ ăn khá ổn, lên món nhanh, không gian hơi nhỏ và cần cải thiện vệ sinh." },
      { "name": "Huyen Chau Nguyen", "rating": 4, "content": "Menu đa dạng, giá rẻ, sốt vừa miệng. Có lần bị lẫn sốt nhưng vẫn sẽ quay lại." }
    ]
  },
  {
    "name": "Bánh mì thịt xiên nướng",
    "address": "67 Chùa Láng, Láng Thượng (cạnh Laika Coffee)",
    "distance": "200-300m",
    "price": "<30k",
    "type": ["Gà/Thịt chiên", "Bánh mì pate/chảo/muối ớt"],
    "time": ["Chiều", "Tối"],
    "hours": "16:00 - 22:00",
    "menu": [
      { "dish": "Thịt xiên nướng", "price": "10k/xiên" },
      { "dish": "Bánh mì thịt xiên nướng", "price": "25k/ổ" }
    ],
    "reviews": [
      { "name": "Admin U", "rating": 4, "content": "Thịt xiên ngon, ăn kèm bánh mì khá ổn." }
    ]
  },
  {
    "name": "HTX Thịt Xiên Nướng Hoàng Đức",
    "address": "55 Phố Chùa Láng, Láng Thượng",
    "distance": "200-300m",
    "price": "<30k",
    "type": ["Gà/Thịt chiên"],
    "time": ["Chiều", "Tối"],
    "hours": "11:00 - 13:00, 16:00 - 19:30",
    "menu": [
      { "dish": "Thịt xiên heo", "price": "13k/xiên" },
      { "dish": "Thịt xiên gà (mua từ 5 xiên)", "price": "13k/xiên" },
      { "dish": "Cánh gà (mua từ 5 miếng)", "price": "11k-30k" }
    ],
    "reviews": [
      { "name": "Son Dao", "rating": 4, "content": "Xiên thịt vừa chín tới, nóng hổi. Trà ngon nhưng khẩu phần hơi ít." },
      { "name": "lamkaoo", "rating": 3, "content": "Thịt xiên đậm vị, nhưng các món khác chưa đặc sắc." }
    ]
  },
  {
    "name": "Bánh mì chảo Phúc Linh",
    "address": "78 Phố Chùa Láng, Láng Thượng, Đống Đa, Hà Nội",
    "distance": "200m",
    "price": ">50k",
    "type": ["Bánh mì pate/chảo/muối ớt"],
    "time": ["Sáng", "Trưa", "Chiều", "Tối"],
    "hours": "07:30 - 22:00",
    "menu": [
      { "dish": "Bánh mì chảo sốt truyền thống", "price": "50k" },
      { "dish": "Bánh mì chảo sốt tiêu nấm", "price": "50k" },
      { "dish": "Chảo bò đặc biệt", "price": "85k" },
      { "dish": "Gọi thêm: Pate", "price": "15k" },
      { "dish": "Gọi thêm: Trứng", "price": "8k" },
      { "dish": "Gọi thêm: Thịt", "price": "10k" },
      { "dish": "Gọi thêm: Xúc xích", "price": "10k" }
    ],
    "reviews": [
      { "name": "Quang Tiến", "rating": 4, "content": "Bánh mì giòn, phục vụ dễ chịu, không gian hơi chật." },
      { "name": "Huong Nguyen", "rating": 5, "content": "Quán nhỏ nhưng ngon, được refill sốt miễn phí." }
    ]
  },
  {
    "name": "Chà bá lửa",
    "address": "44 Ngõ 59 Chùa Láng, Láng Thượng, Đống Đa",
    "distance": "300-400m",
    "price": "<30k",
    "type": ["Bánh mì pate/chảo/muối ớt"],
    "time": ["Sáng", "Trưa", "Chiều", "Tối"],
    "hours": "08:00 - 23:00",
    "menu": [
      { "dish": "Vị truyền thống", "price": "20k-30k" },
      { "dish": "Vị đặc biệt (best seller)", "price": "25k-35k" },
      { "dish": "Full topping", "price": "35k-45k" },
      { "dish": "Laya trứng muối", "price": "15k" }
    ],
    "reviews": [
      { "name": "Kim Ngân Trần", "rating": 4, "content": "Bánh mì muối ớt ổn, nhiều topping, hợp giới trẻ." },
      { "name": "Sơn Phạm Trường", "rating": 4, "content": "Đồ ăn ngon nhưng quán hơi khó tìm, chỗ ngồi hơi chật." }
    ]
  },
  {
    "name": "Bánh mì One One",
    "address": "87 Phố Chùa Láng, Đống Đa, Hà Nội",
    "distance": "Cạnh cổng trường FTU",
    "price": "<30k",
    "type": ["Bánh mì pate/chảo/muối ớt"],
    "time": ["Cả ngày"],
    "hours": "06:30 - 21:30",
    "menu": [
      { "dish": "Bánh mì pate nhân trứng", "price": "20k-30k" },
      { "dish": "Combo bánh mì + trà tắc", "price": "30k-35k" }
    ],
    "reviews": [
      { "name": "MindControl KMC", "rating": 4, "content": "Bánh mì nhiều nhân, dễ tìm." },
      { "name": "Admin Review", "rating": 4, "content": "Quán quen sinh viên, đông nhưng combo 30k khá ngon." }
    ]
  },
  {
    "name": "Bánh mì chả cá",
    "address": "Phía tay trái từ cổng trường",
    "distance": "100m",
    "price": "<30k",
    "type": ["Bánh mì pate/chảo/muối ớt"],
    "time": ["Sáng", "Trưa"],
    "hours": "09:00 - 15:00",
    "menu": [
      { "dish": "Bánh mì chả cá/trứng", "price": "16k" },
      { "dish": "Bánh mì thập cẩm", "price": "25k" },
      { "dish": "Combo bánh + sữa gạo", "price": "30k-35k" }
    ],
    "reviews": [
      { "name": "Admin U", "rating": 4, "content": "Bánh ngon, nên mua combo. Nên đi sớm để đồ nóng." }
    ]
  },
  {
    "name": "Bánh mì Pew Pew",
    "address": "1 Ngõ 84 Phố Chùa Láng, Láng Thượng",
    "distance": "300-400m",
    "price": "<30k",
    "type": ["Bánh mì pate/chảo/muối ớt"],
    "time": ["Sáng", "Trưa", "Chiều", "Tối"],
    "hours": "06:00 - 21:00",
    "menu": [
      { "dish": "Bánh mì cóc", "price": "15k" },
      { "dish": "Bánh mì thập cẩm (best seller)", "price": "35k" },
      { "dish": "Bánh mì gà mật ong", "price": "35k" },
      { "dish": "Bánh mì bò tiêu đen", "price": "35k" }
    ],
    "reviews": [
      { "name": "Thế Anh Nguyễn", "rating": 4, "content": "Bánh mì thập cẩm khá hợp vị." },
      { "name": "Taiga Akimoto", "rating": 5, "content": "Giá rẻ, bánh giòn, nhân viên chuyên nghiệp." }
    ]
  },
  {
    "name": "Bánh cuốn gia truyền Huyền Anh",
    "address": "Số 1 Ngõ 84, Phố Chùa Láng, Láng Thượng",
    "distance": "300-400m",
    "price": "<30k",
    "type": ["Bánh cuốn"],
    "time": ["Sáng", "Trưa", "Chiều", "Tối"],
    "hours": "06:00 - 22:30",
    "menu": [
      { "dish": "Bánh cuốn thường", "price": "25k" },
      { "dish": "Bánh cuốn chả quế", "price": "30k" }
    ],
    "reviews": [
      { "name": "LamKaoo", "rating": 3, "content": "Giá rẻ nhưng chất lượng ở mức tạm, không gian hơi bí." },
      { "name": "Thuận Trần", "rating": 3, "content": "Ăn tạm ổn, không quá xuất sắc." }
    ]
  },
  {
    "name": "Bánh cuốn nóng bún chả",
    "address": "29 Ngõ 185 Phố Chùa Láng, Láng Thượng, Đống Đa",
    "distance": "600m",
    "price": "<30k",
    "type": ["Bánh cuốn"],
    "time": ["Sáng", "Trưa"],
    "hours": "09:00 - 15:00",
    "menu": [
      { "dish": "Bánh cuốn chả quế", "price": "25k" },
      { "dish": "Bánh cuốn chả nướng/trứng chả quế", "price": "30k" }
    ],
    "reviews": [
      { "name": "Thưởng Công", "rating": 3, "content": "Bánh cuốn ổn, nước chấm vừa miệng nhưng cần chú ý vệ sinh." }
    ]
  }
]

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_restaurant' not in st.session_state:
    st.session_state.selected_restaurant = None
if 'filters' not in st.session_state:
    st.session_state.filters = {
        'distance': 'Tất cả',
        'price': 'Tất cả',
        'type': 'Tất cả',
        'time': 'Tất cả'
    }

st.markdown("""
<style>
/* Style cho button trong navbar */
div[data-testid="column"] button {
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #ffffff;
    background-color: #ff7a00;
    border-radius: 12px;
    padding: 12px 0;
    border: none;
}

/* Hover effect */
div[data-testid="column"] button:hover {
    background-color: #e86c00;
    color: #ffffff;
}

/* Button đang được click */
div[data-testid="column"] button:focus {
    box-shadow: 0 0 0 0.2rem rgba(255, 122, 0, 0.4);
}
</style>
""", unsafe_allow_html=True)

# Navigation function
def navigate_to(page):
    st.session_state.page = page
    # Only keep selected_restaurant if going to detail page
    if page != 'detail':
        st.session_state.selected_restaurant = None
    st.rerun()

# Navigation Bar
def render_navbar():
    # Title
    st.markdown('<div class="navbar-title">🍜 HÔM NAY ĂN GÌ?</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    pages = {
        'home': 'Trang chủ',
        'search': 'Tìm quán',
        'about': 'Về dự án',
        'contribute': 'Đóng góp'
    }
    
    cols = st.columns(len(pages))
    for i, (page_key, page_name) in enumerate(pages.items()):
        with cols[i]:
            if st.button(page_name, key=f"nav_{page_key}", use_container_width=True):
                navigate_to(page_key)

# Page 1: Home
def render_home():
    # Hero Section
    st.markdown("""
    <div class="hero">
        <div class="hero-title2">Giới thiệu nhanh</div>
        <div class="hero-subtitle2">Website hỗ trợ sinh viên lựa chọn quán ăn quanh khu vực Chùa Láng</div>
        <p class="hero-description">
            "Hôm Nay Ăn Gì?" là nền tảng giúp sinh viên, đặc biệt là sinh viên Ngoại Thương, nhanh chóng tìm được quán ăn phù hợp trong bán kính 0–2km quanh Chùa Láng dựa trên giá cả, thời gian, khoảng cách và trải nghiệm thực tế từ sinh viên.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # About Preview
    st.markdown('<div class="hero-title2">Đặc điểm nổi bật</div>', unsafe_allow_html=True)
    
    preview_cols = st.columns(4)
    previews = [
        ("⚡", "Tìm quán ăn nhanh chóng"),
        ("🎓", "Dữ liệu do sinh viên thu thập"),
        ("💰", "Phù hợp ngân sách sinh viên"),
        ("✨", "Giao diện đơn giản, dễ sử dụng")
    ]
    
    for col, (icon, text) in zip(preview_cols, previews):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <p class="feature-description">{text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown('<div class="hero-title2">Các tính năng chính</div>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🔍",
            "title": "Tìm kiếm thông minh",
            "description": "Lọc quán ăn theo nhiều tiêu chí."
        },
        {
            "icon": "📍",
            "title": "Bản đồ vị trí",
            "description": "Xem vị trí quán ăn và khoảng cách từ Chùa Láng."
        },
        {
            "icon": "⭐",
            "title": "Review thực tế",
            "description": "Đánh giá trực tiếp từ sinh viên, không quảng cáo."
        },
        {
            "icon": "⏱",
            "title": "Gợi ý theo thời gian",
            "description": "Gợi ý quán cho bữa sáng, trưa, tối, khuya."
        }
    ]
    
    feature_cols = st.columns(2)
    for idx, feature in enumerate(features):
        with feature_cols[idx % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <div class="feature-title">{feature['title']}</div>
                <p class="feature-description">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Page 2: Search/Explore
def render_search():
    st.markdown('<div class="hero-title3">Bộ lọc</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        distance_filter = st.selectbox(
            "Khoảng cách",
            ["Tất cả", "<500m", "500m-1km", "1-2km"],
            key="distance_filter"
        )
    
    with col2:
        price_filter = st.selectbox(
            "Mức giá",
            ["Tất cả", "<30k", "30-40k", "40-50k", ">50k"],
            key="price_filter"
        )
    
    with col3:
        type_filter = st.selectbox(
            "Loại món",
            ["Tất cả", "Cơm/Xôi/Cháo", "Bún/Phở/Miến/Bánh canh/Súp", "Gà/Thịt chiên", "Đồ Hàn", "Nem nướng", "Bánh mì pate/chảo/muối ớt", "Bánh tráng", "Tacos", "Bánh cuốn"],
            key="type_filter"
        )
    
    with col4:
        time_filter = st.selectbox(
            "Thời gian",
            ["Tất cả", "Sáng", "Trưa", "Tối", "Khuya"],
            key="time_filter"
        )
    
    if st.button("Áp dụng bộ lọc", use_container_width=True):
        st.session_state.filters = {
            'distance': distance_filter,
            'price': price_filter,
            'type': type_filter,
            'time': time_filter
        }
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter restaurants
    filtered_restaurants = restaurants_data.copy()
    
    if st.session_state.filters['distance'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['distance'] == st.session_state.filters['distance']]
    
    if st.session_state.filters['price'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['price'] == st.session_state.filters['price']]
    
    if st.session_state.filters['type'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['type'] in r['type']]
    
    if st.session_state.filters['time'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['time'] in r['time']]
    
    # Display results
    st.markdown(
        f'''
        <div class="hero-title3">
            Kết quả ({len(filtered_restaurants)} quán)
        </div>
        ''',
        unsafe_allow_html=True
    )
        
    if len(filtered_restaurants) == 0:
        st.info("Không tìm thấy quán nào phù hợp với bộ lọc của bạn. Hãy thử thay đổi tiêu chí tìm kiếm!")
    else:
        for restaurant in filtered_restaurants:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3 class="restaurant-name">{restaurant['name']}</h3>
                    <p class="restaurant-address">📍 {restaurant['address']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Use unique key for each button and store restaurant data before navigating
                if st.button("Xem chi tiết", key=f"view_{restaurant['name']}", use_container_width=True):
                    st.session_state.selected_restaurant = restaurant
                    st.session_state.page = 'detail'
                    st.rerun()

# Page 3: Restaurant Detail
def render_detail():
    if st.session_state.selected_restaurant is None:
        st.markdown('<h2 class="section-title">Chưa chọn quán</h2>', unsafe_allow_html=True)
        st.info("Vui lòng chọn một quán từ trang Tìm quán để xem chi tiết!")
        st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)
        if st.button("Đi đến trang Tìm quán", use_container_width=True):
            navigate_to('search')
        return
    
    restaurant = st.session_state.selected_restaurant
    
    # Back button
    if st.button("<-  Quay lại danh sách"):
        navigate_to('search')
    
    st.markdown(f'<h2 class="section-title">{restaurant["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #666; font-size: 1.1rem; margin-top: -1rem;">📍 {restaurant["address"]}</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Thông tin chi tiết
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Thông tin chi tiết</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Khoảng cách:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['distance']} từ Chùa Láng</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Mức giá:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['price']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Giờ mở cửa:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['hours']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="margin-bottom: 1rem;">
        <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Loại món:</p>
        <p style="font-family: 'DM Sans', sans-serif; color: #666;">{', '.join(restaurant['type'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Menu tiêu biểu
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Menu tiêu biểu</h3>', unsafe_allow_html=True)
    
    for item in restaurant['menu']:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.8rem 0; border-bottom: 1px solid #f0f0f0;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.2rem;">🍽️</span>
                <span style="font-family: 'DM Sans', sans-serif; color: #333; font-size: 1rem;">{item['dish']}</span>
            </div>
            <span style="font-family: 'DM Sans', sans-serif; color: #ff6b6b; font-weight: 700; font-size: 1.1rem;">{item['price']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Đánh giá từ sinh viên
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Đánh giá từ sinh viên</h3>', unsafe_allow_html=True)

    for review in restaurant["reviews"]:
        stars = "⭐" * review["rating"]

        st.markdown(f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="margin-bottom: 0.5rem;">
                <span style="color:#ffa500; font-size:1.2rem;">
                    {stars}
                </span>
                <span style="font-weight:700; margin-left:0.5rem;">
                    - {review["name"]}
                </span>
            </div>
            <p style="color:#666; font-style:italic;">
                "{review["content"]}"
            </p>
        </div>
        """, unsafe_allow_html=True)

# Page 4: About Project
def render_about():
    st.markdown('<div class="hero-title3">Giới thiệu dự án</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-card">
        <p class="feature-description">
            "Hôm Nay Ăn Gì?" là dự án được nhóm sinh viên Trường Đại học Ngoại thương xây dựng nhằm hỗ trợ sinh viên lựa chọn quán ăn phù hợp 
            quanh khu vực Chùa Láng. Dự án xuất phát từ nhu cầu thực tế của sinh viên. đặc biệt là tân sinh viên khi 
            mới nhập học gặp khó khăn trong việc tìm địa điểm ăn uống phù hợp với ngân sách 
            và thời gian rảnh của mình.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-title3">Mục tiêu</div>', unsafe_allow_html=True)
    
    goals = [
        "Hỗ trợ sinh viên tìm quán trong bán kính 0–2km",
        "Cho phép lọc theo giá, loại món, thời gian",
        "Cung cấp thông tin ngắn gọn, tập trung trải nghiệm thật",
        "Áp dụng kiến thức Python vào sản phẩm thực tế"
    ]
    
    for goal in goals:
        st.markdown(f"""
        <div class="restaurant-card">
            <p class="feature-description">{goal}</p>
        </div>
        """, unsafe_allow_html=True)
    
# Page 5: Contribute
def render_contribute():   
    with st.form("contribute_form"):
        st.markdown('<div class="hero-title3">Thông tin quán ăn</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Tên quán *", placeholder="VD: Cơm Tấm Sài Gòn")
            address = st.text_input("Địa chỉ *", placeholder="VD: 123 Chùa Láng, Đống Đa")
            price = st.selectbox("Giá trung bình *", ["<30k", "30-50k", ">50k"])
        
        with col2:
            food_type = st.multiselect(
                "Loại món *",
                ["Cơm", "Bún", "Phở", "Mì", "Đồ ăn vặt", "Trà sữa", "Xôi", "Lẩu"]
            )
            time_slots = st.multiselect(
                "Thời gian phục vụ *",
                ["Sáng", "Trưa", "Tối", "Khuya"]
            )
            rating = st.slider("Đánh giá của bạn", 1.0, 5.0, 4.0, 0.5)
        
        review = st.text_area(
            "Đánh giá ngắn *",
            placeholder="Chia sẻ trải nghiệm của bạn về quán này...",
            height=150
        )
        
        submit = st.form_submit_button("Gửi đánh giá", use_container_width=True)
        
        if submit:
            if name and address and food_type and time_slots and review:
                st.success("Cảm ơn bạn đã đóng góp! Thông tin của bạn đã được ghi nhận.")
                st.balloons()
            else:
                st.error("Vui lòng điền đầy đủ các thông tin bắt buộc (*)")

# Main App Logic
def main():
    render_navbar()
    
    # Route to appropriate page
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'search':
        render_search()
    elif st.session_state.page == 'detail':
        render_detail()
    elif st.session_state.page == 'about':
        render_about()
    elif st.session_state.page == 'contribute':
        render_contribute()

if __name__ == "__main__":
    main()
