import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Textile Machine Identification App",
    page_icon="🧵",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #F5F7FA;
    }

    .title {
        color: #12355B;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #4F6D7A;
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #D9E2EC;
        margin-bottom: 15px;
    }

    .machine-name {
        color: #0B6E4F;
        font-size: 26px;
        font-weight: 700;
    }

    .stage {
        color: #D35400;
        font-weight: 700;
    }

    .lab-box {
        background-color: #EEF4F8;
        padding: 15px;
        border-radius: 10px;
    }

    .footer {
        text-align: center;
        color: #6B7280;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MACHINE DATABASE
# ---------------------------------------------------------
machines = [
    {
        "Machine": "Uniclean B11",
        "Model": "B11",
        "Stage": "Blow Room",
        "Manufacturer": "Trützschler",
        "Function": "Opening and cleaning textile fiber.",
        "Working": "Fiber tufts are opened and impurities are removed before carding.",
        "LAB_L": 55,
        "LAB_a": 4,
        "LAB_b": 8
    },
    {
        "Machine": "Carding Machine",
        "Model": "TC 11",
        "Stage": "Carding",
        "Manufacturer": "Trützschler",
        "Function": "Individualizes fibers and removes remaining impurities.",
        "Working": "Fibers pass through carding elements where they are opened, cleaned and formed into sliver.",
        "LAB_L": 62,
        "LAB_a": 3,
        "LAB_b": 12
    },
    {
        "Machine": "Drawing Machine",
        "Model": "IDF",
        "Stage": "Drawing",
        "Manufacturer": "Rieter",
        "Function": "Improves fiber parallelization and sliver uniformity.",
        "Working": "Several slivers are combined and drafted through roller pairs.",
        "LAB_L": 48,
        "LAB_a": 2,
        "LAB_b": 10
    },
    {
        "Machine": "Simplex / Roving Frame",
        "Model": "FA415A",
        "Stage": "Roving",
        "Manufacturer": "Marzoli",
        "Function": "Produces roving from drawn sliver.",
        "Working": "The sliver is drafted, twisted and wound onto a roving bobbin.",
        "LAB_L": 50,
        "LAB_a": 5,
        "LAB_b": 15
    },
    {
        "Machine": "Ring Spinning Machine",
        "Model": "G 38",
        "Stage": "Spinning",
        "Manufacturer": "Rieter",
        "Function": "Converts roving into yarn.",
        "Working": "Roving is drafted, twisted and wound onto a bobbin to produce yarn.",
        "LAB_L": 45,
        "LAB_a": 6,
        "LAB_b": 14
    },
    {
        "Machine": "Autoconer",
        "Model": "RM 338",
        "Stage": "Winding",
        "Manufacturer": "Rieter",
        "Function": "Winds yarn from spinning bobbins onto packages.",
        "Working": "Yarn is unwound, faults are detected and removed, then yarn is wound onto a package.",
        "LAB_L": 58,
        "LAB_a": 1,
        "LAB_b": 7
    },
    {
        "Machine": "Warping Machine",
        "Model": "Benninger",
        "Stage": "Warping",
        "Manufacturer": "Benninger",
        "Function": "Prepares warp yarn for weaving.",
        "Working": "Yarns are collected from packages and arranged parallel on a warp beam.",
        "LAB_L": 52,
        "LAB_a": 4,
        "LAB_b": 11
    },
    {
        "Machine": "Sizing Machine",
        "Model": "KSH",
        "Stage": "Sizing",
        "Manufacturer": "Benninger",
        "Function": "Applies size material to warp yarn.",
        "Working": "Warp yarn passes through size solution, drying and sizing zones before winding onto a beam.",
        "LAB_L": 57,
        "LAB_a": 3,
        "LAB_b": 9
    },
    {
        "Machine": "Air-Jet Loom",
        "Model": "JAT 810",
        "Stage": "Weaving",
        "Manufacturer": "Toyota",
        "Function": "Produces woven fabric.",
        "Working": "Warp and weft yarns are interlaced using an air-jet insertion system.",
        "LAB_L": 60,
        "LAB_a": 2,
        "LAB_b": 6
    }
]

df = pd.DataFrame(machines)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="title">🧵 Textile Machine Identification App</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Learn Textile Machines, Models, Functions & Working Processes</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.title("⚙️ Machine Explorer")

stages = ["All Stages"] + sorted(df["Stage"].unique())

selected_stage = st.sidebar.selectbox(
    "Select Process Stage",
    stages
)

search = st.sidebar.text_input(
    "🔎 Search Machine / Model",
    placeholder="Example: RM 338"
)

# ---------------------------------------------------------
# FILTER DATA
# ---------------------------------------------------------
filtered_df = df.copy()

if selected_stage != "All Stages":
    filtered_df = filtered_df[
        filtered_df["Stage"] == selected_stage
    ]

if search:
    filtered_df = filtered_df[
        filtered_df["Machine"].str.contains(search, case=False, na=False)
        | filtered_df["Model"].str.contains(search, case=False, na=False)
        | filtered_df["Manufacturer"].str.contains(search, case=False, na=False)
    ]

# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Machines", len(df))
col2.metric("Process Stages", df["Stage"].nunique())
col3.metric("Manufacturers", df["Manufacturer"].nunique())
col4.metric("Search Results", len(filtered_df))

st.divider()

# ---------------------------------------------------------
# MACHINE SELECTION
# ---------------------------------------------------------
if len(filtered_df) > 0:

    machine_names = filtered_df["Machine"].tolist()

    selected_machine = st.selectbox(
        "🧵 Select Machine",
        machine_names
    )

    machine = filtered_df[
        filtered_df["Machine"] == selected_machine
    ].iloc[0]

    # -----------------------------------------------------
    # MACHINE INFORMATION
    # -----------------------------------------------------
    st.markdown(
        f'<div class="machine-name">{machine["Machine"]}</div>',
        unsafe_allow_html=True
    )

    st.write(
        f'**Model:** {machine["Model"]}  |  '
        f'**Stage:** {machine["Stage"]}  |  '
        f'**Manufacturer:** {machine["Manufacturer"]}'
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ⚙️ Function")
        st.info(machine["Function"])

    with col2:
        st.markdown("### 🔄 Working Process")
        st.success(machine["Working"])

    # -----------------------------------------------------
    # LAB VALUES
    # -----------------------------------------------------
    st.markdown("### 🎨 Machine Color — CIE L*a*b* Values")

    lab1, lab2, lab3 = st.columns(3)

    lab1.metric("L* — Lightness", machine["LAB_L"])
    lab2.metric("a* — Green ↔ Red", machine["LAB_a"])
    lab3.metric("b* — Blue ↔ Yellow", machine["LAB_b"])

    st.markdown(
        f"""
        <div class="lab-box">
        <b>LAB Value:</b>
        L* = {machine["LAB_L"]},
        a* = {machine["LAB_a"]},
        b* = {machine["LAB_b"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # MACHINE IMAGE UPLOAD
    # -----------------------------------------------------
    st.markdown("### 📷 Machine Image")

    uploaded_image = st.file_uploader(
        "Upload a machine image for learning",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        st.image(
            uploaded_image,
            caption=f"{machine['Machine']} — Uploaded Image",
            width=600
        )

else:
    st.warning("No machine found. Try another machine name, model or stage.")

# ---------------------------------------------------------
# MACHINE DATABASE TABLE
# ---------------------------------------------------------
st.divider()

st.markdown("### 📚 Textile Machine Database")

display_df = filtered_df[
    ["Machine", "Model", "Stage", "Manufacturer"]
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------------
# LEARNING TIPS
# ---------------------------------------------------------
st.divider()

st.markdown("### 💡 Learning Tip")

st.info(
    "Use the Search box to practice remembering machine names and model "
    "numbers. Select different process stages to study the complete textile "
    "manufacturing sequence."
)

# ---------------------------------------------------------
# PROCESS FLOW
# ---------------------------------------------------------
st.markdown("### 🔄 Textile Manufacturing Process")

st.write(
    "Blow Room → Carding → Drawing → Roving → Spinning → "
    "Winding → Warping → Sizing → Weaving"
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    '<div class="footer">Textile Engineering Learning Application | '
    'Built with Streamlit</div>',
    unsafe_allow_html=True
)
