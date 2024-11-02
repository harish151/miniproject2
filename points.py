import re
def suggestion(data1,data2):
    list1 = []
    list2 = []
    m1,m2=0,0
    #list1 - mobile data1
    list1.append(data1['gsmPlatformDetails'].get('platformOs'))
    list1.append(data1['gsmPlatformDetails'].get('platformChipset'))
    list1.append(data1['gsmPlatformDetails'].get('platformCpu'))
    list1.append(data1['gsmPlatformDetails'].get('platformGpu'))
    list1.append(data1['gsmMemoryDetails'].get('memoryInternal'))
    list1.append(list(data1['gsmMainCameraDetails'].values())[1])
    list1.append(data1['gsmMainCameraDetails'].get('mainCameraVideo'))
    list1.append(data1['gsmSelfieCameraDetails'].get('selfieCameraSingle'))
    list1.append(data1['gsmSelfieCameraDetails'].get('selfieCameraVideo'))
    list1.append(data1['gsmBatteryDetails'].get('batteryType'))
    list1.append(data1['gsmBatteryDetails'].get('batteryCharging'))
    list1.append(data1['gsmMiscDetails'].get('miscPrice'))
    #list2 - mobile data2
    list2.append(data2['gsmPlatformDetails'].get('platformOs'))
    list2.append(data2['gsmPlatformDetails'].get('platformChipset'))
    list2.append(data2['gsmPlatformDetails'].get('platformCpu'))
    list2.append(data2['gsmPlatformDetails'].get('platformGpu'))
    list2.append(data2['gsmMemoryDetails'].get('memoryInternal'))
    list2.append(list(data2['gsmMainCameraDetails'].values())[1])
    list2.append(data2['gsmMainCameraDetails'].get('mainCameraVideo'))
    list2.append(data2['gsmSelfieCameraDetails'].get('selfieCameraSingle'))
    list2.append(data2['gsmSelfieCameraDetails'].get('selfieCameraVideo'))
    list2.append(data2['gsmBatteryDetails'].get('batteryType'))
    list2.append(data2['gsmBatteryDetails'].get('batteryCharging'))
    list2.append(data2['gsmMiscDetails'].get('miscPrice'))
    
    for i,j in zip(list1,list2):
        m1_values = re.findall(r'\d+', i)
        m2_values = re.findall(r'\d+', j)
        if m1_values < m2_values:
            m2=m2+1
        elif m1_values > m2_values:
            m1=m1+1
        else:
            m1,m2=m1+1,m2+1
    
    #compare score
    if m1<m2:
        return f"{data2['phoneDetails']['brandValue']} {data2['phoneDetails']['modelValue']}"
    elif m1>m2:
        return f"{data1['phoneDetails']['brandValue']} {data1['phoneDetails']['modelValue']}"
    else:
        return f"both {data1['phoneDetails']['brandValue']} {data1['phoneDetails']['modelValue']} and {data2['phoneDetails']['brandValue']} {data2['phoneDetails']['modelValue']}"
    
