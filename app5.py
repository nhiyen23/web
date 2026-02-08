import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

# Cấu hình trang
st.set_page_config(
    page_title="Hôm Nay Ăn Gì?",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #4ECDC4;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .restaurant-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Dữ liệu mẫu về quán ăn
@st.cache_data
def load_restaurant_data():
    restaurants = [
        {
            "name": "Cơm Tấm Sài Gòn",
            "address": "123 Láng Hạ, Đống Đa",
            "distance": 0.3,
            "price_range": "20-35k",
            "avg_price": 28,
            "food_type": ["Cơm", "Cơm tấm"],
            "rating": 4.5,
            "open_time": "6:00-22:00",
            "meals": ["Sáng", "Trưa", "Tối"],
            "menu": [
                {"item": "Cơm tấm sườn", "price": "30k"},
                {"item": "Cơm tấm bì", "price": "28k"},
                {"item": "Cơm tấm đặc biệt", "price": "35k"}
            ],
            "reviews": [
                "Giá rẻ, phục vụ nhanh, hợp ăn trưa",
                "Cơm ngon, sườn mềm, nước mắm vừa miệng"
            ],
            "lat": 21.0145,
            "lng": 105.8076
        },
        {
            "name": "Phở Bò 24",
            "address": "45 Tôn Thất Tùng, Đống Đa",
            "distance": 0.5,
            "price_range": "30-45k",
            "avg_price": 35,
            "food_type": ["Phở", "Bún"],
            "rating": 4.7,
            "open_time": "5:30-23:00",
            "meals": ["Sáng", "Trưa", "Tối", "Khuya"],
            "menu": [
                {"item": "Phở bò tái", "price": "35k"},
                {"item": "Phở bò chín", "price": "35k"},
                {"item": "Phở đặc biệt", "price": "45k"}
            ],
            "reviews": [
                "Phở ngon, nước trong, thịt mềm",
                "Mở cửa sớm, tiện ăn sáng"
            ],
            "lat": 21.0125,
            "lng": 105.8065
        },
        {
            "name": "Bún Chả Hà Nội",
            "address": "67 Nguyễn Lương Bằng, Đống Đa",
            "distance": 0.8,
            "price_range": "25-40k",
            "avg_price": 30,
            "food_type": ["Bún", "Bún chả"],
            "rating": 4.6,
            "open_time": "10:00-21:00",
            "meals": ["Trưa", "Tối"],
            "menu": [
                {"item": "Bún chả", "price": "30k"},
                {"item": "Bún chả giò", "price": "35k"},
                {"item": "Nem rán", "price": "5k/cái"}
            ],
            "reviews": [
                "Chả nướng thơm, nước mắm ngon",
                "Quán đông khách, nên đi sớm"
            ],
            "lat": 21.0155,
            "lng": 105.8095
        },
        {
            "name": "Mì Quảng Đà Nẵng",
            "address": "89 Láng Hạ, Đống Đa",
            "distance": 0.4,
            "price_range": "30-50k",
            "avg_price": 38,
            "food_type": ["Mì", "Mì Quảng"],
            "rating": 4.4,
            "open_time": "9:00-21:00",
            "meals": ["Trưa", "Tối"],
            "menu": [
                {"item": "Mì Quảng gà", "price": "35k"},
                {"item": "Mì Quảng tôm thịt", "price": "40k"},
                {"item": "Bánh tráng trộn", "price": "25k"}
            ],
            "reviews": [
                "Mì Quảng đúng vị, không gian sạch sẽ",
                "Giá hơi cao nhưng ngon"
            ],
            "lat": 21.0140,
            "lng": 105.8070
        },
        {
            "name": "Trà Sữa TocoToco",
            "address": "12 Nguyễn Chí Thanh, Đống Đa",
            "distance": 0.6,
            "price_range": "25-45k",
            "avg_price": 32,
            "food_type": ["Trà sữa", "Đồ uống"],
            "rating": 4.3,
            "open_time": "8:00-23:00",
            "meals": ["Sáng", "Trưa", "Tối", "Khuya"],
            "menu": [
                {"item": "Trà sữa truyền thống", "price": "28k"},
                {"item": "Trà sữa trân châu", "price": "32k"},
                {"item": "Matcha latte", "price": "35k"}
            ],
            "reviews": [
                "Trà sữa ngon, không gian thoải mái",
                "Phù hợp ngồi học nhóm"
            ],
            "lat": 21.0165,
            "lng": 105.8085
        },
        {
            "name": "Bánh Mì Que",
            "address": "34 Tôn Thất Tùng, Đống Đa",
            "distance": 0.3,
            "price_range": "15-25k",
            "avg_price": 20,
            "food_type": ["Bánh mì", "Đồ ăn vặt"],
            "rating": 4.8,
            "open_time": "6:00-22:00",
            "meals": ["Sáng", "Trưa", "Tối"],
            "menu": [
                {"item": "Bánh mì thịt", "price": "20k"},
                {"item": "Bánh mì trứng", "price": "15k"},
                {"item": "Bánh mì pate", "price": "18k"}
            ],
            "reviews": [
                "Bánh mì giá sinh viên, ngon bổ rẻ",
                "Quán nhỏ nhưng đông khách"
            ],
            "lat": 21.0135,
            "lng": 105.8068
        },
        {
            "name": "Lẩu Nướng Hàn Quốc",
            "address": "78 Láng Hạ, Đống Đa",
            "distance": 1.2,
            "price_range": "80-150k",
            "avg_price": 110,
            "food_type": ["Lẩu", "Nướng"],
            "rating": 4.5,
            "open_time": "11:00-23:00",
            "meals": ["Trưa", "Tối"],
            "menu": [
                {"item": "Buffet lẩu nướng", "price": "99k"},
                {"item": "Buffet cao cấp", "price": "149k"}
            ],
            "reviews": [
                "Buffet đa dạng, phù hợp đi nhóm",
                "Giá cao nhưng xứng đáng"
            ],
            "lat": 21.0180,
            "lng": 105.8100
        },
        {
            "name": "Xôi Chè Hà Nội",
            "address": "23 Nguyễn Lương Bằng, Đống Đa",
            "distance": 0.7,
            "price_range": "10-30k",
            "avg_price": 18,
            "food_type": ["Xôi", "Chè", "Đồ ăn vặt"],
            "rating": 4.4,
            "open_time": "6:00-22:00",
            "meals": ["Sáng", "Trưa", "Tối"],
            "menu": [
                {"item": "Xôi xéo", "price": "15k"},
                {"item": "Xôi gà", "price": "25k"},
                {"item": "Chè đậu đỏ", "price": "12k"}
            ],
            "reviews": [
                "Xôi ngon, giá rẻ, ăn sáng tuyệt",
                "Chè ngọt vừa phải"
            ],
            "lat": 21.0160,
            "lng": 105.8090
        }
    ]
    return pd.DataFrame(restaurants)

# Load data
df_restaurants = load_restaurant_data()

# Sidebar navigation
st.sidebar.title("📍 Menu")
page = st.sidebar.radio(
    "Chọn trang:",
    ["🏠 Trang chủ", "🔍 Tìm quán ăn", "🏪 Chi tiết quán", "📊 Thống kê", 
     "💡 Về dự án", "👥 Nhóm thực hiện", "📩 Đóng góp"]
)

# ===========================================
# TRANG 1: TRANG CHỦ
# ===========================================
if page == "🏠 Trang chủ":
    st.markdown('<p class="main-header">🍜 HÔM NAY ĂN GÌ?</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Web hỗ trợ sinh viên lựa chọn quán ăn quanh khu vực Chùa Láng</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Hero section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 👋 Chào mừng bạn đến với "Hôm Nay Ăn Gì?"
        
        "Hôm Nay Ăn Gì?" là nền tảng giúp sinh viên, đặc biệt là sinh viên **Ngoại Thương**, 
        nhanh chóng tìm được quán ăn phù hợp trong bán kính **1–2km quanh Chùa Láng** 
        dựa trên giá cả, thời gian, khoảng cách và trải nghiệm thực tế từ sinh viên.
        
        🎯 **Không còn phải băn khoăn mỗi bữa ăn nữa!**
        """)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔍 Bắt đầu tìm quán", use_container_width=True):
                st.session_state.page = "🔍 Tìm quán ăn"
                st.rerun()
        with col_btn2:
            if st.button("📋 Xem danh sách quán", use_container_width=True):
                st.session_state.page = "🔍 Tìm quán ăn"
                st.rerun()
    
    with col2:
        st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400", 
                caption="Khám phá ẩm thực quanh Chùa Láng")
    
    st.markdown("---")
    
    # Giới thiệu nhanh
    st.markdown("### 🌟 Tại sao chọn chúng tôi?")
    
    cols = st.columns(4)
    features_preview = [
        {"icon": "⚡", "title": "Tìm kiếm nhanh", "desc": "Hỗ trợ tìm quán ăn nhanh chóng"},
        {"icon": "👥", "title": "Dữ liệu thực tế", "desc": "Do sinh viên tự thu thập và đánh giá"},
        {"icon": "💰", "title": "Phù hợp SV", "desc": "Phù hợp ngân sách sinh viên"},
        {"icon": "🎨", "title": "Dễ sử dụng", "desc": "Giao diện đơn giản, thân thiện"}
    ]
    
    for col, feature in zip(cols, features_preview):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h2 style="text-align: center;">{feature['icon']}</h2>
                <h4 style="text-align: center; margin: 0.5rem 0;">{feature['title']}</h4>
                <p style="text-align: center; font-size: 0.9rem;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Các tính năng chính
    st.markdown("### 🎯 Các tính năng chính")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🔍 Tìm kiếm thông minh
        Lọc quán theo giá, khoảng cách, loại món và thời gian ăn.
        
        #### 📍 Bản đồ vị trí
        Xem vị trí quán ăn và khoảng cách từ Chùa Láng.
        """)
    
    with col2:
        st.markdown("""
        #### ⭐ Review thực tế
        Đánh giá trực tiếp từ sinh viên, không quảng cáo.
        
        #### ⏱ Gợi ý theo thời gian
        Gợi ý quán cho bữa sáng, trưa, tối, ăn vặt.
        """)
    
    st.markdown("---")
    
    # Statistics preview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏪 Tổng số quán", len(df_restaurants))
    with col2:
        st.metric("💵 Giá TB", f"{int(df_restaurants['avg_price'].mean())}k")
    with col3:
        st.metric("⭐ Đánh giá TB", f"{df_restaurants['rating'].mean():.1f}/5")

# ===========================================
# TRANG 2: TÌM QUÁN ĂN
# ===========================================
elif page == "🔍 Tìm quán ăn":
    st.title("🔍 Tìm quán ăn phù hợp")
    
    st.markdown("### Bộ lọc tìm kiếm")
    
    # Bộ lọc
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        distance_filter = st.selectbox(
            "📍 Khoảng cách",
            ["Tất cả", "<500m", "500m-1km", "1-2km"]
        )
    
    with col2:
        price_filter = st.selectbox(
            "💰 Mức giá",
            ["Tất cả", "<30k", "30-50k", ">50k"]
        )
    
    with col3:
        all_food_types = set()
        for types in df_restaurants['food_type']:
            all_food_types.update(types)
        food_type_filter = st.selectbox(
            "🍜 Loại món",
            ["Tất cả"] + sorted(list(all_food_types))
        )
    
    with col4:
        meal_filter = st.selectbox(
            "⏰ Thời gian",
            ["Tất cả", "Sáng", "Trưa", "Tối", "Khuya"]
        )
    
    # Áp dụng bộ lọc
    filtered_df = df_restaurants.copy()
    
    if distance_filter != "Tất cả":
        if distance_filter == "<500m":
            filtered_df = filtered_df[filtered_df['distance'] < 0.5]
        elif distance_filter == "500m-1km":
            filtered_df = filtered_df[(filtered_df['distance'] >= 0.5) & (filtered_df['distance'] < 1)]
        else:  # 1-2km
            filtered_df = filtered_df[(filtered_df['distance'] >= 1) & (filtered_df['distance'] <= 2)]
    
    if price_filter != "Tất cả":
        if price_filter == "<30k":
            filtered_df = filtered_df[filtered_df['avg_price'] < 30]
        elif price_filter == "30-50k":
            filtered_df = filtered_df[(filtered_df['avg_price'] >= 30) & (filtered_df['avg_price'] <= 50)]
        else:  # >50k
            filtered_df = filtered_df[filtered_df['avg_price'] > 50]
    
    if food_type_filter != "Tất cả":
        filtered_df = filtered_df[filtered_df['food_type'].apply(lambda x: food_type_filter in x)]
    
    if meal_filter != "Tất cả":
        filtered_df = filtered_df[filtered_df['meals'].apply(lambda x: meal_filter in x)]
    
    st.markdown("---")
    
    # Hiển thị kết quả
    st.markdown(f"### 📋 Tìm thấy {len(filtered_df)} quán phù hợp")
    
    if len(filtered_df) == 0:
        st.warning("Không tìm thấy quán ăn phù hợp với bộ lọc. Hãy thử điều chỉnh bộ lọc!")
    else:
        # Hiển thị danh sách quán
        for idx, row in filtered_df.iterrows():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3>🍽️ {row['name']}</h3>
                    <p><strong>📍 Địa chỉ:</strong> {row['address']}</p>
                    <p><strong>🚶 Khoảng cách:</strong> {row['distance']}km | 
                       <strong>💵 Giá TB:</strong> {row['avg_price']}k | 
                       <strong>⭐ Đánh giá:</strong> {row['rating']}/5</p>
                    <p><strong>🍜 Loại món:</strong> {', '.join(row['food_type'])}</p>
                    <p><strong>⏰ Phù hợp:</strong> {', '.join(row['meals'])}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button(f"Xem chi tiết", key=f"detail_{idx}"):
                    st.session_state.selected_restaurant = idx
                    st.session_state.page = "🏪 Chi tiết quán"
                    st.rerun()

# ===========================================
# TRANG 3: CHI TIẾT QUÁN ĂN
# ===========================================
elif page == "🏪 Chi tiết quán":
    st.title("🏪 Chi tiết quán ăn")
    
    # Chọn quán để xem chi tiết
    selected_idx = st.selectbox(
        "Chọn quán để xem chi tiết:",
        range(len(df_restaurants)),
        format_func=lambda x: df_restaurants.iloc[x]['name']
    )
    
    if 'selected_restaurant' in st.session_state:
        selected_idx = st.session_state.selected_restaurant
    
    restaurant = df_restaurants.iloc[selected_idx]
    
    # Thông tin cơ bản
    st.markdown(f"## 🍽️ {restaurant['name']}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        ### 📋 Thông tin cơ bản
        
        - **📍 Địa chỉ:** {restaurant['address']}
        - **🚶 Khoảng cách từ Chùa Láng:** {restaurant['distance']}km
        - **💰 Mức giá:** {restaurant['price_range']} (TB: {restaurant['avg_price']}k)
        - **🕐 Giờ mở cửa:** {restaurant['open_time']}
        - **🍜 Loại món:** {', '.join(restaurant['food_type'])}
        - **⏰ Phù hợp:** {', '.join(restaurant['meals'])}
        - **⭐ Đánh giá:** {restaurant['rating']}/5
        """)
    
    with col2:
        # Hiển thị bản đồ (giả lập)
        st.markdown("### 📍 Vị trí trên bản đồ")
        st.markdown(f"""
        <iframe
            width="100%"
            height="300"
            frameborder="0"
            style="border:0"
            src="https://www.google.com/maps?q={restaurant['lat']},{restaurant['lng']}&output=embed"
            allowfullscreen>
        </iframe>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu tiêu biểu
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📜 Menu tiêu biểu")
        for item in restaurant['menu']:
            st.markdown(f"- **{item['item']}**: {item['price']}")
    
    with col2:
        st.markdown("### 💬 Đánh giá từ sinh viên")
        st.markdown(f"**⭐ Đánh giá trung bình: {restaurant['rating']}/5**")
        for review in restaurant['reviews']:
            st.info(f"💭 {review}")

# ===========================================
# TRANG 4: THỐNG KÊ
# ===========================================
elif page == "📊 Thống kê":
    st.title("📊 Tổng quan dữ liệu")
    
    # Thống kê tổng quan
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <h1>{len(df_restaurants)}</h1>
            <p>Tổng số quán</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <h1>{int(df_restaurants['avg_price'].mean())}k</h1>
            <p>Giá trung bình</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <h1>{df_restaurants['rating'].mean():.1f}</h1>
            <p>Đánh giá TB</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-box">
            <h1>{df_restaurants['distance'].mean():.1f}km</h1>
            <p>Khoảng cách TB</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Biểu đồ
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🍜 Phân bố loại món")
        food_types = []
        for types in df_restaurants['food_type']:
            food_types.extend(types)
        food_type_counts = pd.Series(food_types).value_counts()
        
        fig = px.pie(
            values=food_type_counts.values,
            names=food_type_counts.index,
            title="Các loại món phổ biến",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 💰 Phân bố giá")
        fig = px.histogram(
            df_restaurants,
            x='avg_price',
            nbins=10,
            title="Phân bố mức giá trung bình",
            labels={'avg_price': 'Giá (nghìn đồng)'},
            color_discrete_sequence=['#FF6B6B']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Biểu đồ thời gian
    st.markdown("### ⏰ Khung giờ phù hợp")
    meals_count = {"Sáng": 0, "Trưa": 0, "Tối": 0, "Khuya": 0}
    for meals in df_restaurants['meals']:
        for meal in meals:
            meals_count[meal] = meals_count.get(meal, 0) + 1
    
    fig = px.bar(
        x=list(meals_count.keys()),
        y=list(meals_count.values()),
        title="Số quán phù hợp theo khung giờ",
        labels={'x': 'Bữa ăn', 'y': 'Số quán'},
        color=list(meals_count.values()),
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Biểu đồ khoảng cách vs giá
    st.markdown("### 📊 Mối quan hệ giữa khoảng cách và giá")
    fig = px.scatter(
        df_restaurants,
        x='distance',
        y='avg_price',
        size='rating',
        color='rating',
        hover_data=['name'],
        title="Khoảng cách vs Giá (Size: Đánh giá)",
        labels={'distance': 'Khoảng cách (km)', 'avg_price': 'Giá TB (nghìn đồng)'},
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig, use_container_width=True)

# ===========================================
# TRANG 5: VỀ DỰ ÁN
# ===========================================
elif page == "💡 Về dự án":
    st.title("💡 Về dự án")
    
    st.markdown("""
    ## 📖 Giới thiệu dự án
    
    **"Hôm Nay Ăn Gì?"** được xây dựng nhằm hỗ trợ sinh viên lựa chọn quán ăn phù hợp 
    quanh khu vực Chùa Láng. Dự án xuất phát từ nhu cầu thực tế của sinh viên khi mới 
    nhập học, gặp khó khăn trong việc tìm địa điểm ăn uống phù hợp với ngân sách và thời gian.
    
    ---
    
    ## 🎯 Mục tiêu
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ✅ Xây dựng web hỗ trợ sinh viên tìm quán trong bán kính 1–2km
        
        ✅ Cho phép lọc theo giá, loại món, thời gian
        """)
    
    with col2:
        st.markdown("""
        ✅ Cung cấp thông tin ngắn gọn, tập trung trải nghiệm thật
        
        ✅ Áp dụng kiến thức Python vào sản phẩm thực tế
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 👥 Đối tượng sử dụng
    
    - **Sinh viên Đại học Ngoại Thương Hà Nội**
    - **Sinh viên các trường trong khu vực Chùa Láng**
    - **Người dân sinh sống và làm việc quanh khu vực**
    
    ---
    
    ## 🛠️ Công nghệ sử dụng
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🐍</h3>
            <h4 style="text-align: center;">Python</h4>
            <p style="text-align: center; font-size: 0.9rem;">Ngôn ngữ chính</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🎈</h3>
            <h4 style="text-align: center;">Streamlit</h4>
            <p style="text-align: center; font-size: 0.9rem;">Web framework</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">📊</h3>
            <h4 style="text-align: center;">Pandas</h4>
            <p style="text-align: center; font-size: 0.9rem;">Xử lý dữ liệu</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h3 style="text-align: center;">🗺️</h3>
            <h4 style="text-align: center;">Google Maps</h4>
            <p style="text-align: center; font-size: 0.9rem;">Hiển thị bản đồ</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📈 Kế hoạch phát triển
    
    - 🔄 Cập nhật thường xuyên dữ liệu quán ăn mới
    - 🤖 Tích hợp chatbot tư vấn tự động
    - 📱 Phát triển ứng dụng mobile
    - 🎁 Thêm tính năng khuyến mãi, deal sinh viên
    - 🌐 Mở rộng ra các khu vực khác
    """)

# ===========================================
# TRANG 6: NHÓM THỰC HIỆN
# ===========================================
elif page == "👥 Nhóm thực hiện":
    st.title("👥 Nhóm thực hiện")
    
    st.markdown("""
    ### 🎓 Đội ngũ phát triển dự án "Hôm Nay Ăn Gì?"
    
    Chúng tôi là nhóm sinh viên Đại học Ngoại Thương, đam mê công nghệ và muốn 
    giải quyết vấn đề thực tế của cộng đồng sinh viên.
    """)
    
    st.markdown("---")
    
    # Thông tin thành viên (có thể tùy chỉnh)
    team_members = [
        {
            "name": "Nguyễn Văn A",
            "role": "Team Leader & Backend Developer",
            "responsibilities": "Quản lý dự án, phát triển hệ thống backend",
            "avatar": "👨‍💻"
        },
        {
            "name": "Trần Thị B",
            "role": "Data Analyst & Collector",
            "responsibilities": "Thu thập và phân tích dữ liệu quán ăn",
            "avatar": "👩‍💼"
        },
        {
            "name": "Lê Văn C",
            "role": "Frontend Developer",
            "responsibilities": "Thiết kế giao diện và trải nghiệm người dùng",
            "avatar": "👨‍🎨"
        },
        {
            "name": "Phạm Thị D",
            "role": "Content Creator & Reviewer",
            "responsibilities": "Viết nội dung và review quán ăn",
            "avatar": "👩‍✍️"
        }
    ]
    
    cols = st.columns(2)
    
    for idx, member in enumerate(team_members):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <h1 style="text-align: center; font-size: 4rem; margin: 0;">{member['avatar']}</h1>
                <h3 style="text-align: center; color: #FF6B6B; margin: 0.5rem 0;">{member['name']}</h3>
                <h4 style="text-align: center; color: #4ECDC4; margin: 0.5rem 0;">{member['role']}</h4>
                <p style="text-align: center; margin-top: 1rem;">{member['responsibilities']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📧 Liên hệ với chúng tôi
    
    - **Email:** homnayanghi@gmail.com
    - **Facebook:** facebook.com/homnayanghi
    - **Địa chỉ:** Đại học Ngoại Thương, Chùa Láng, Đống Đa, Hà Nội
    
    💡 **Lưu ý:** Thông tin trên chỉ mang tính chất minh họa. Bạn có thể thay đổi tên và vai trò 
    của các thành viên theo nhóm thực tế của mình.
    """)

# ===========================================
# TRANG 7: ĐÓNG GÓP DỮ LIỆU
# ===========================================
elif page == "📩 Đóng góp":
    st.title("📩 Đóng góp dữ liệu")
    
    st.markdown("""
    ### 🙏 Cảm ơn bạn đã muốn đóng góp!
    
    Dữ liệu của bạn sẽ giúp cộng đồng sinh viên có thêm nhiều lựa chọn tốt hơn.
    Vui lòng điền đầy đủ thông tin dưới đây:
    """)
    
    st.markdown("---")
    
    # Form đóng góp
    with st.form("contribution_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            restaurant_name = st.text_input("🏪 Tên quán ăn *", placeholder="VD: Phở Bò Hà Nội")
            address = st.text_input("📍 Địa chỉ *", placeholder="VD: 123 Láng Hạ, Đống Đa")
            price = st.text_input("💰 Giá trung bình *", placeholder="VD: 30k hoặc 25-40k")
        
        with col2:
            food_types = st.multiselect(
                "🍜 Loại món *",
                ["Cơm", "Phở", "Bún", "Mì", "Bánh mì", "Trà sữa", "Đồ ăn vặt", "Lẩu", "Nướng", "Xôi", "Chè", "Khác"]
            )
            rating = st.slider("⭐ Đánh giá của bạn", 1.0, 5.0, 4.0, 0.5)
            distance = st.number_input("🚶 Khoảng cách từ Chùa Láng (km)", 0.1, 5.0, 0.5, 0.1)
        
        meals = st.multiselect(
            "⏰ Phù hợp bữa ăn",
            ["Sáng", "Trưa", "Tối", "Khuya"]
        )
        
        review = st.text_area(
            "💬 Đánh giá ngắn của bạn *",
            placeholder="VD: Quán ngon, giá cả phải chăng, phục vụ nhiệt tình...",
            height=100
        )
        
        st.markdown("**(*) Các trường bắt buộc**")
        
        submitted = st.form_submit_button("📤 Gửi đóng góp", use_container_width=True)
        
        if submitted:
            if restaurant_name and address and price and food_types and review:
                st.success(f"""
                ✅ **Cảm ơn bạn đã đóng góp!**
                
                Thông tin về **{restaurant_name}** đã được ghi nhận. 
                Chúng tôi sẽ xem xét và cập nhật vào hệ thống sớm nhất!
                """)
                
                st.balloons()
                
                # Hiển thị thông tin đã gửi
                with st.expander("Xem thông tin bạn vừa gửi"):
                    st.write(f"**Tên quán:** {restaurant_name}")
                    st.write(f"**Địa chỉ:** {address}")
                    st.write(f"**Giá:** {price}")
                    st.write(f"**Loại món:** {', '.join(food_types)}")
                    st.write(f"**Đánh giá:** {rating}/5")
                    st.write(f"**Khoảng cách:** {distance}km")
                    st.write(f"**Bữa ăn:** {', '.join(meals) if meals else 'Chưa chọn'}")
                    st.write(f"**Review:** {review}")
            else:
                st.error("⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (*)")
    
    st.markdown("---")
    
    st.markdown("""
    ### 💡 Gợi ý khi đánh giá
    
    - Chia sẻ trải nghiệm thực tế của bạn
    - Đề cập đến chất lượng món ăn, giá cả, phục vụ
    - Gợi ý món ngon nên thử
    - Lưu ý về thời gian đông khách
    - Đề cập không gian quán (rộng/nhỏ, ồn/yên tĩnh)
    
    **🙏 Mọi đóng góp của bạn đều rất có giá trị!**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 2rem 0;'>
    <p>🍜 Hôm Nay Ăn Gì? - Dự án hỗ trợ sinh viên Chùa Láng</p>
    <p>Được phát triển với ❤️ bởi sinh viên Ngoại Thương</p>
    <p style='font-size: 0.8rem;'>© 2024 All rights reserved</p>
</div>
""", unsafe_allow_html=True)
