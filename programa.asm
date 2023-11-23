.data

clase_c STRUCT
    propertyc1 DD ?     
    propertyc2 DQ ?
clase_c END


clase_a STRUCT
    propertya1 DD ?     
    propertya2 DQ ?     
    propertyc1 DD ?     
    propertyc2 DQ ?
clase_a END


clase_b STRUCT
    propertyb3 DD ?     
    propertyb4 DQ ?     
    propertya1 DD ?     
    propertya2 DQ ?     
    propertyc1 DD ?     
    propertyc2 DQ ?
clase_b END

c2 clase_a <>
c1 clase_a <>
c4 clase_b <>
c3 clase_b <>
b DD ?
a DD ?