function themthuoc(id,name,gia,soLuong){
    event.preventDefault()

    fetch('/api/them_thuoc',{
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': name,
            'gia': gia,
            'soLuong': soLuong
        }),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(function(res)
    {
        console.info(res)
        return res.json()
    }).then(function(data){
        console.info(data)
    }).catch(function(err){
        console.error(err)
    })
}