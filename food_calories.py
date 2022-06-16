import streamlit as st
import pandas as pd
food_groups={
    'Diary':['Milk🥛','Yogurt🧉','Cheese🧀','ChocoMilk🍫','String Cheese🧀','Smoothie🍹'],
    'Vegetables':['Broccoli🥦','Cucumber🥒','Carrot🥕','Mushroom🍄','Sweet Potato🥔','Lettuce🥬'],
    'Fruits':['Apple🍎','Banana🍌','Cherry🍒','Avocado🥑','Kiwifruit🥝','Berries🫐'],
    'Grains':['Berley🌾','Oats🌾','Wheat🌾','White Rice🌾','Corn🌾','Brown Rice🌾'],
    'Protein':['Eggs🥚','Tuna🐠','Chicken🍗','Pork🍖','Salmon🍣','Beef🥩']
    }

food_groups_display=pd.DataFrame(food_groups,index=['1','2','3','4','5','6'])

st.title("Healty App")
st.caption("The purpose of this app is to inform what types of food you should have to eat in your daily life and help to calculate the calories of foods you eat.")

st.header("Food Groups 🧀🥕🥑🌾🍗")
st.caption("There are five major food groups and the indegrients of each group are not same. This following table displays some foods contataining in each group.")
food_groups_display

diary_cal=pd.read_json('diary_calories.json')
diary_cal_show=pd.DataFrame(diary_cal)
st.header("Calories from diaries")
st.caption("The calories contained in different diary products are not same. Some diary products provide high calories and you should choose and consume diary products according to your calories requirement.")
diary_cal_show

vege_cal=pd.read_json('vege_calories.json')
vege_cal_show=pd.DataFrame(vege_cal)
st.header("Calories from vegetables")
st.caption("The calories contained in different vegetables are not same. Some vegetables provide high calories and you should choose and consume vegetables according to your calories requirement.")
vege_cal_show

fruits_cal=pd.read_json('fruits_calories.json')
fruits_cal_show=pd.DataFrame(fruits_cal)
st.header("Calories from fruits")
st.caption("The calories contained in different fruits are not same. Some fruits provide high calories and you should choose and consume fruits  according to your calories requirement.")
fruits_cal_show

grains_cal=pd.read_json('grains_calories.json')
grains_cal_show=pd.DataFrame(grains_cal)
st.header("Calories from grains")
st.caption("The calories contained in different grains are not same. Some grains provide high calories and you should choose and consume grains products according to your calories requirement.")
grains_cal_show

protein_cal=pd.read_json('protein_calories.json')
protein_cal_show=pd.DataFrame(protein_cal)
st.header("Calories from proteins")
st.caption("The calories contained in different meats are not same. Some meats provide high calories and you should choose and consume protein products according to your calories requirement.")
protein_cal_show
