import niezgody
z discord.ext.commands import Bot
z poleceń importu discord.ext
z discord.ext.commands.cooldowns importuj BucketType
import asyncio
platforma importowa
import colorys
importuj losowo
import os
czas importu
z discord.voice_client import VoiceClient
z gry importu dyskietek, Osadź, Kolor, Status, Typ kanału


Forbidden = discord.Embed (title = "Permission Denied", description = "1) Sprawdź, czy masz uprawnienie do wykonania tej czynności n2) Sprawdź, czy moja rola ma uprawnienia do wykonania tej czynności na tym kanale, czy nie n3) Proszę sprawdzić moją pozycję w roli. ", kolor = 0x00ff00)
client = Bot (description = "DarkBot Bot jest najlepszy", command_prefix = "d!", pm_help = True)
client.remove_command („pomoc”)


async def status_task ():
    podczas gdy prawda:
        oczekuj client.change_presence (game = discord.Game (name = 'for d! help'))
        poczekaj na asyncio.sleep (5)
        oczekuj client.change_presence (game = discord.Game (name = 'with' + str (len (set (client.get_all_members ())))) + 'users'))
        poczekaj na asyncio.sleep (5)
        czekaj na client.change_presence (game = discord.Game (name = 'in' + str (len (client.servers)) + 'servers'))
        poczekaj na asyncio.sleep (5)
        

	
@ client.event
async def on_ready ():
    print ('Zalogowany jako' + client.user.name + '(ID:' + client.user.id + ') | Połączony z' + str (len (client.servers)) + 'server | Connected to' + str ( len (set (client.get_all_members ()))) + „użytkownicy”)
    wydrukować('--------')
    wydrukować('--------')
    drukuj („Started Dark BOT”)
    drukuj („Utworzony przez Utkarsha”)
    client.loop.create_task (status_task ())


  
	
def is_owner (ctx):
    return ctx.message.author.id == "420525168381657090, 395535610548322326"

def is_dark (ctx):
    return ctx.message.author.id == "420525168381657090"

def is_shreyas (ctx):
    zwróć ctx.message.author.id == "376602841625919488"

def is_gameworld (ctx):
    zwróć ctx.message.author.id == "402075464694366211"

def is_ranger (ctx):
    zwróć ctx.message.author.id == "304911836460089345"

@ client.command (pass_context = True)
@ commands.check (is_owner)
async def restart ():
    poczekaj na client.logout ()

@ client.event
async def on_message (wiadomość):
	czekaj na client.process_commands (wiadomość)

@ client.event
async def on_member_join (członek):
    drukuj („Na naszym serwerze” + nazwa użytkownika + „właśnie dołączył”)
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (color = discord.Color ((r << 16) + (g << 8) + b))
    embed.set_author (name = 'Welcome message')
    embed.add_field (name = '__Witamy na naszym serwerze __', value = '** Mam nadzieję, że będziesz aktywny tutaj. Sprawdź nasze reguły serwera i nigdy nie próbuj łamać żadnych reguł. ”, inline = False)
    embed.set_image (url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    czekaj na client.send_message (członek, embed = embed)
    print ("Wysłano wiadomość do" + nazwa.członka)
    channel = discord.utils.get (client.get_all_channels (), server__name = 'DarkBot Official Server', name = 'darkbot-servers-join-leave-log')
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = f'Welcome {member.name} to {member.server.name} ', description =' Nie zapomnij sprawdzić <# 474572305192845312> i nigdy nie próbuj łamać żadnego z nich ', kolor = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = '__ Dziękujemy za dołączenie__', value = '** Mam nadzieję, że będziesz aktywny tutaj. **', inline = True)
    embed.add_field (name = 'Twoja pozycja dołączenia to', value = member.joined_at)
    embed.set_image (url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail (url = member.avatar_url)
    czekaj na client.send_message (kanał, embed = embed)


@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)

async def unbanall (ctx):
    server = ctx.message.server
    ban_list = czekaj na client.get_bans (serwer)
    await client.say ('Unbanning {} members'.format (len (ban_list)))
    dla członka w ban_list:
        poczekaj na client.unban (serwer, członek)
	
@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True) 

@ commands.cooldown (rate = 5, per = 86400, type = BucketType.user) 
async def access (ctx, member: discord.Member):
    role = discord.utils.get (member.server.roles, name = 'Access')
    czekaj na client.add_roles (członek, rola)
    embed = discord.Embed (title = "Użytkownik ma dostęp!", description = "** {0} ** uzyskało dostęp z ** {1} **!". format (członek, ctx.message.author), kolor = 0xff00f6)
    czekaj na client.say (embed = embed)
    poczekaj na asyncio.sleep (45 * 60)
    czekaj na client.remove_roles (członek, rola)
	

	
@ client.command (pass_context = True)  
@ commands.has_permissions (kick_members = True)
async def getuser (ctx, rola: discord.Role = None):
    jeśli rola jest Brak:
        await client.say („Na tym serwerze nie ma roli„ STAFF ”!”)
        powrót
    empty = True
    dla członka w ctx.message.server.members:
        jeśli rola w member.roles:
            await client.say ("{0.name}: {0.id}". format (członek))
            pusty = Fałsz
    jeśli jest pusta:
        await client.say („Nikt nie ma roli {}”. format (role.mention))
	
@ client.command (pass_context = True)
async def play (ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    próbować:
        vc = czekaj na client.join_voice_channel (voice_channel)
        msg = await client.say („Ładowanie ...”)
        player = czekaj na vc.create_ytdl_player ("ytsearch:" + url)
        player.start ()
        await client.say („Udana załadowana piosenka!”)
        poczekaj na client.delete_message (msg)
    z wyjątkiem wyjątku jako e:
        drukuj (e)
        czekaj na klienta.say („Ponowne połączenie”)
        dla x w client.voice_clients:
            if (x.server == ctx.message.server):
                oczekuj x.disconnect ()
                nvc = czekaj na client.join_voice_channel (voice_channel)
                msg = await client.say („Ładowanie ...”)
                player2 = czekaj na nvc.create_ytdl_player ("ytsearch:" + url)
                player2.start ()

@ client.command (pass_context = True)
@ commands.check (is_dark)
async def dmall (ctx, *, msg: str):
    dla server_member w ctx.message.server.members:
      poczekaj na client.send_message (server_member, msg)
      poczekaj na client.delete_message (ctx.message)
		
@ client.command (pass_context = True)
async def stop (ctx):
    dla x w client.voice_clients:
        if (x.server == ctx.message.server):
            return await x.disconnect ()

    return await client.say („Nie gram anyting ???!”)

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def joinvoice (ctx):
    author = ctx.message.author
    channel = author.voice_channel
    poczekaj na client.join_voice_channel (kanał)

@ client.command (pass_context = True, aliasy = ['em', 'e'])
async def modmail (ctx, *, msg = None):
    channel = discord.utils.get (client.get_all_channels (), name = '📬mod-mails📬')
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    color = discord.Color ((r << 16) + (g << 8) + b)
    jeśli nie msg:
        await client.say („Proszę podać wiadomość do wysłania”)
    jeszcze:
        poczekaj na client.send_message (kanał, embed = discord.Embed (color = color, description = msg + 'n Wiadomość From-' + ctx.message.author.id))
        poczekaj na client.delete_message (ctx.message)
    powrót

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)     
async def userinfo (ctx, użytkownik: discord.Member):
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "{} 's info" .format (user.name), description = "Oto, co mogłem znaleźć.", color = discord.Color ((r << 16) + (g < <8) + b))
    embed.add_field (name = "Name", value = user.name, inline = True)
    embed.add_field (name = "ID", value = user.id, inline = True)
    embed.add_field (name = "Status", value = user.status, inline = True)
    embed.add_field (name = "Najwyższa rola", value = user.top_role)
    embed.add_field (name = „Dołączył”, value = user.joined_at)
    embed.set_thumbnail (url = user.avatar_url)
    czekaj na client.say (embed = embed)
    
@ client.command (pass_context = True)
@ commands.check (is_dark)
async def iamdark (ctx):
    author = ctx.message.author
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Utkarsh Kumar')
    poczekaj na client.add_roles (ctx.message.author, role)
    drukuj („Dodano ciemną rolę w '+ (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
	
@ client.command (pass_context = True)
@ commands.check (is_shreyas)
async def iamshreyas (ctx):
    author = ctx.message.author
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'ShreyasMF')
    poczekaj na client.add_roles (ctx.message.author, role)
    drukuj („Dodano rolę SHREYAS w '+ (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)

@ client.command (pass_context = True)
@ commands.check (is_ranger)
async def iamgameworld (ctx):
    author = ctx.message.author
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Gameworld')
    poczekaj na client.add_roles (ctx.message.author, role)
    drukuj ('Dodano rolę GAMEWORLD w' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
	
@ client.command (pass_context = True)
@ commands.check (is_ranger)
async def iamnotranger (ctx):
    author = ctx.message.author
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Dark Ranger')
    czekaj na client.remove_roles (ctx.message.author, role)
    print ('Usunięta rola DarkRanger w' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)

@ client.command (pass_context = True)
async def registerme (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "Successfully added", description = "REGISTERED role", color = discord.Color ((r << 16) + (g << 8) + b))
    embed.set_image (url = 'https://preview.ibb.co/e3iyap/ezgif_3_7dcc4d6bec.gif')
    embed.add_field (name = "Enjoy!", value = "Dzięki za rejestrację w Mini Militia Tournament", inline = True)
    
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'W4w tourney ”)
    poczekaj na client.add_roles (ctx.message.author, role)
    drukuj ('Dodano rolę ZAREJESTROWANĄ w' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
    
@ client.command (pass_context = True)
async def iamcoder (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "Successfully added", description = "Programmer role", color = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = "Enjoy!", value = "Happy Coding :-). Tutaj otrzymasz specjalną pomoc od naszych pracowników związaną z rozwojem serwera.", inline = True)
    
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Programmer')
    poczekaj na client.add_roles (ctx.message.author, role)
    print ('Dodano rolę codów w' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
    
@ client.command (pass_context = True)
async def iamnotcoder (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "Successfully remove", description = "Programmer role", color = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = "Enjoy!", value = "Mam nadzieję, że wypróbujesz również inne nasze funkcje", inline = True)
    
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Programmer')
    czekaj na client.remove_roles (ctx.message.author, role)
    print ('Usunięta rola codów z' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
 
@ client.command (pass_context = True)
async def iamnotserverdeveloper (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "Successfully remove", description = "Server developer role", color = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = "Enjoy!", value = "Mam nadzieję, że wypróbujesz również inne nasze funkcje", inline = True)
    
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Server Developer')
    czekaj na client.remove_roles (ctx.message.author, role)
    print ('Usunięta rola programisty serwera z' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
    

@ client.command (pass_context = True)
async def iamserverdeveloper (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (title = "Successfully added", description = "Server Developer role", color = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = "Enjoy!", value = "Happy Server Development. Tutaj otrzymasz specjalną pomoc od naszego zespołu wsparcia związanego z rozwojem serwera", inline = True)
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Server Developer')
    poczekaj na client.add_roles (ctx.message.author, role)
    print ('Dodano rolę codów w' + (ctx.message.author.name))
    poczekaj na client.send_message (autor, embed = embed)
 
	
@ client.command (pass_context = True)

@ commands.has_permissions (manage_roles = True)     
async def role (ctx, user: discord.Member, *, role: discord.Role = None):
        jeśli rola jest Brak:
            return await client.say („Nie określiłeś roli!”)

        jeśli rola nie jest w user.roles:
            czekaj na client.add_roles (użytkownik, rola)
            return await client.say ("rola {} została dodana do {}.". format (rola, użytkownik))

        jeśli rola w user.roles:
            czekaj na client.remove_roles (użytkownik, rola)
            return await client.say („rola {} została usunięta z {}.”. format (rola, użytkownik))
 
@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def warn (ctx, userName: discord.User, *, message: str): 
    poczekaj na client.send_message (userName, "Zostałeś ostrzeżony o: ** {} **". format (wiadomość))
    await client.say (": warning: __ ** {0} zostało ostrzeżone! ** __: ostrzeżenie: ** Powód: {1} **" .format (nazwa_użytkownika, wiadomość))
    przechodzić

@ client.command (pass_context = True)
async def ownerinfo (ctx):
    embed = discord.Embed (title = "Informacje o właścicielu", opis = "Nazwa Bot-DarkBot", kolor = 0x00ff00)
    embed.set_footer (tekst = „Copyright @ UK Soft”)
    embed.set_author (name = "Nazwa właściciela bota - DarkLegend # 3807, | Sunny Singh | ™ ✓ # 4856, Tag <! - Wstecz -> # 1488 nID: 420525168381657090,395535610548322326,399274658027012098")
    embed.add_field (name = "Site- https://bit.ly/darkbotauth", value = "Dzięki za dodanie naszego bota", inline = True)
    czekaj na client.say (embed = embed)
    
@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)
async def def (ctx):
    author = ctx.message.author
    server = ctx.message.server
    mod_perms = discord.Permissions (manage_messages = True, kick_members = True, manage_nicknames = True, mute_members = True)
    admin_perms = discord.Permissions (ADMINISTRATOR = True)

    poczekaj na client.create_role (author.server, name = "Owner", permissions = admin_perms)
    poczekaj na client.create_role (author.server, name = "Admin", permissions = admin_perms)
    poczekaj na client.create_role (author.server, name = „Senior Moderator”, permissions = mod_perms)
    poczekaj na client.create_role (author.server, name = "GOH")
    poczekaj na client.create_role (author.server, name = „Moderator”, permissions = mod_perms)
    poczekaj na client.create_role (author.server, name = „Muted”)
    
    poczekaj na client.create_role (author.server, name = „Friend of Owner”)
    poczekaj na client.create_role (author.server, name = „Verified”)
    everyone_perms = discord.PermissionOverwrite (send_messages = False, read_messages = True)
    everyone = discord.ChannelPermissions (target = server.default_role, overwrite = everyone_perms)
    user_perms = discord.PermissionOverwrite (read_messages = True)
    user = discord.ChannelPermissions (target = server.default_role, overwrite = user_perms)
    private_perms = discord.PermissionOverwrite (read_messages = False)
    private = discord.ChannelPermissions (target = server.default_role, overwrite = private_perms)    
    poczekaj na client.create_channel (serwer, „🎉welcome”, wszyscy)
    poczekaj na client.create_channel (serwer, „🎯rules🎯”, wszyscy)
    poczekaj na client.create_channel (serwer, „🎥featured-content🎥”, wszyscy)
    poczekaj na client.create_channel (serwer, „📢announcements📢”, wszyscy)
    poczekaj na client.create_channel (serwer, „otevote_polls📢”, wszyscy)
    poczekaj na client.create_channel (serwer, „private_chat”, prywatny)
    poczekaj na client.create_channel (serwer, „🎮general_chat🎮”, użytkownik)
    poczekaj na client.create_channel (serwer, „🎮general_media🎮”, użytkownik)
    poczekaj na client.create_channel (serwer, „👍bots_zone👍”, użytkownik)
    poczekaj na client.create_channel (serwer, „outyoutube_links🎥”, użytkownik)
    poczekaj na client.create_channel (serwer, „🎥giveaway_links🎥”, użytkownik)
    poczekaj na client.create_channel (serwer, „🎥other_links🎥”, użytkownik)
    poczekaj na client.create_channel (serwer, „🔥Music Zone🔥”, wpisz = discord.ChannelType.voice)
    poczekaj na client.create_channel (serwer, „🔥music_command🔥s”, użytkownik)
    poczekaj na client.create_channel (serwer „hillChill Zone🔥”, wpisz = discord.ChannelType.voice)
    
@ client.command (pass_context = True)
@ commands.has_permissions (manage_nicknames = True)     
async def setnick (ctx, użytkownik: discord.Member, *, nickname):
    czekaj na client.change_nickname (użytkownik, nick)
    poczekaj na client.delete_message (ctx.message)

@ client.command (pass_context = True)
async def poll (ctx, pytanie, * opcje: str):
        jeśli len (opcje) <= 1:
            await client.say („Aby sondować więcej niż jedną opcję!”)
            powrót
        jeśli len (opcje)> 10:
            await client.say („Nie możesz sondować więcej niż 10 rzeczy!”)
            powrót

        jeśli len (opcje) == 2 i opcje [0] == „tak” i opcje [1] == „nie”:
            Reakcje = ['👍', '👎']
        jeszcze:
            reakcje = ['1 u20e3', '2 u20e3', '3 u20e3', '4 u20e3', '5 u20e3', '6 u20e3', '7 u20e3', '8 20e3' , „9 u20e3”, „0001f51f”]

        opis = []
        dla x, opcja w wyliczeniu (opcje):
            opis + = 'n {} {}'. format (reakcje [x], opcja)
            r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
        embed = discord.Embed (title = question, description = ''. join (opis), color = discord.Color ((r << 16) + (g << 8) + b))
        react_message = czekaj na client.say (embed = embed)
        dla reakcji w reakcjach [: len (opcje)]:
            poczekaj na client.add_reaction (react_message, reaction)
        embed.set_footer (text = 'ID ankiety: {}'. format (react_message.id))
        poczekaj na client.edit_message (react_message, embed = embed)
        
@ client.command (pass_context = True)
async def googlefy (ctx, *, msg = None):
    jeśli msg.content == "@everyone":
        powrót
    jeśli msg.content == „@here”:
        powrót
    jeśli nie msg: await client.say („Proszę podać ciąg”)
    jeszcze:
        czekaj na client.say ('http://lmgtfy.com/?q=' + msg)
    powrót

@ client.command (pass_context = True)
async def help (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (color = discord.Color ((r << 16) + (g << 8) + b))
    embed.set_author (name = 'Help')
    embed.set_image (url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field (name = '`` Nasz link do serwera pomocy``' ', value =' https: //discord.gg/vMvv5rr',inline = False)
    embed.add_field (name = 'd! modhelp', value = 'Wyjaśnia wszystkie polecenia, które mogą być używane tylko przez tych, którzy mają uprawnienia do moderacji. Np. Zarządzaj pseudonimami, Zarządzaj wiadomościami, Kick / Ban Members, itp. ”, inline = Fałsz )
    embed.add_field (name = 'd! generalhelp', value = 'Wyjaśnia wszystkie polecenia, które mogą być używane przez wszystkich.', inline = False)
    poczekaj na client.send_message (autor, embed = embed)
    czekaj na client.say ('📨 Sprawdź DMs for Information')
@ client.command (pass_context = True)
async def modhelp (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (color = discord.Color ((r << 16) + (g << 8) + b))
    embed.set_author (name = 'Polecenia moderacji Pomoc')
    embed.set_image (url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field (name = 'd! say (wymagane uprawnienia administratora)', value = 'Użyj go jak `` d! powiedz <text> ``', inline = False)
    embed.add_field (name = 'd! embed (wymagane uprawnienia administratora)', value = 'Użyj go jak `` d! embed <text> ``', inline = False)
    embed.add_field (name = 'd! membercount (Kick member Permission Required)', value = 'Użyj go jak `` d! membercount`` aby uzyskać konto członkowskie', inline = False)
    embed.add_field (name = 'd! removemod (Wymagane uprawnienia administratora)', value = 'Użyj go jak `` d! removemod @ user``, aby usunąć go z mod. Uwaga-Potrzebujesz roli Moderatora na swoim serwerze poniżej darkbot do użyj go. ', inline = False)
    embed.add_field (name = 'd! makemod (Wymagane uprawnienia administratora)', value = 'Użyj go tak, jak `` d! makemod @ user``, aby go zmodyfikować. Uwaga-Do użycia na serwerze musisz mieć rolę Moderatora poniżej darkbot it. ', inline = False)
    embed.add_field (name = 'd! setup (Admin Permission Required)', value = 'Użyj go, aby dodać kanały, kanały głosowe i role, jeśli twój serwer nie jest obecnie rozwijany i masz tylko 1-2 kanały. Uwaga - Użyj go tylko 1 raz Jeśli ponownie użyjesz tego samego polecenia, to znowu zrobi to samo.. Doda prawdziwą kopię poprzednich kanałów + prawdziwą kopię ról wykonanych w poprzednim poleceniu. Więc uważaj. ', inline = False)
    embed.add_field (name = 'd! friend (Admin Permission Required)', value = 'Użyj go jak `` d! friend @ user``, aby dać komuś rolę Friend of Owner', inline = False)
    embed.add_field (name = 'd! role (Manage Roles Permission Required)', value = 'Użyj go jak `` d! role @user <rolename> ``.', inline = False)
    embed.add_field (name = 'd! setnick (wymagane zarządzanie uprawnieniami do pseudonimu)', value = 'Użyj go jak `` d! setnick @ użytkownik <Nowy pseudonim> ``, aby zmienić pseudonim oznaczonego użytkownika.', inline = False )
    embed.add_field (name = 'd! english (Wymagani członkowie Kick Permission)', value = 'Używaj go jak `` d! english @ user``, gdy ktoś mówi w językach innych niż angielski.', inline = False)
    embed.add_field (name = 'd! serverinfo (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! serverinfo``, aby uzyskać informacje o serwerze', inline = False)
    embed.add_field (name = 'd! userinfo (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! userinfo @ user``, aby uzyskać podstawowe informacje o otagowanym użytkowniku', inline = False)
    embed.add_field (name = 'd! kick (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! kick @ user`` aby skopać dowolnego użytkownika', inline = False)
    embed.add_field (name = 'd! role (Wymagane uprawnienia członków Kick'a)', value = 'Użyj go, aby sprawdzić role obecne na serwerze', inline = False)
    embed.add_field (name = 'd! clear (Manage Messages Permission Required)', value = 'Użyj go jak `` d! clear <numer> `` aby usunąć dowolny komunikat', inline = False)
    embed.add_field (name = 'd! mute (Wymagane uprawnienia do wyciszenia członków)', value = 'Użyj go jak `` d! mute @user <time> `` aby wyciszyć dowolnego użytkownika', inline = False)
    embed.add_field (name = 'd! unmute (Wymagane uprawnienia członków)', value = 'Użyj go jak `` d! unmute @ user``, aby anulować wyciszenie kogokolwiek', inline = False)
    embed.add_field (name = 'd! ban (Wymagane uprawnienia członków Ban)', value = 'Użyj go jak `` d! ban @ user``, aby zablokować dowolnego użytkownika', inline = False)
    embed.add_field (name = 'd! rules (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! rules @user <typ naruszenia> `` aby ostrzec użytkownika', inline = False)
    embed.add_field (name = 'd! warn (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! warn @user <typ naruszenia> `` aby ostrzec dowolnego użytkownika', inline = False)    
    embed.add_field (name = 'd! norole (Kick member Permission Required)', value = 'Użyj go jak `` d! norole @ user``, aby ostrzec każdego, kto prosi o promocję', inline = False)
    embed.add_field (name = 'd! getuser (Kick członkowie Permission Wymagane)', value = 'Użyj go jak `` d! getuser @ rolename``, aby uzyskać listę wszystkich użytkowników mających określoną rolę', inline = False)
    poczekaj na client.send_message (autor, embed = embed)
    czekaj na client.say ('📨 Sprawdź DMs for Information')

@ client.command (pass_context = True)
async def generalhelp (ctx):
    author = ctx.message.author
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (color = discord.Color ((r << 16) + (g << 8) + b))
    embed.add_field (name = 'd! poll', value = 'Użyj go jak `` d! poll "Question" "Option1" "Option2" ..... "Option9" ``.', inline = False)
    embed.add_field (name = 'd! guess', value = 'Aby zagrać w grę, użyj `` d! guess <numer> i liczba powinna zawierać się między 1-10``', inline = False)
    embed.add_field (name = 'd! github', value = 'Użyj go jak - `` d! github uksoftworld / DarkBot``', inline = False)
    embed.add_field (name = 'd! bottutorial', value = 'Użyj go jak `` d! bottutorial <nazwa samouczka po darklegend> ``', inline = False)
    embed.add_field (name = 'd! dyno', value = 'Użyj go jak `` d! d! dyno <nazwa polecenia dyno> ``', inline = False)
    embed.add_field (name = 'd! donate', value = 'Użyj go, aby nas przekazać i otrzymać specjalny post na Oficjalnym serwerze DarkBot.', inline = False)
    embed.add_field (name = 'd! ownerinfo', value = 'Aby uzyskać podstawowe informacje o właścicielu.', inline = False)
    embed.add_field (name = 'd! sourcecode', value = 'Użyj go, aby zobaczyć darkbot kod źródłowy.', inline = False)
    embed.add_field (name = 'd! upvote', value = 'Użyj go, aby wzmocnić naszego bota i pomóż nam rosnąć', inline = False)
    embed.add_field (name = 'd! authlink', value = 'Użyj go, aby uzyskać link autoryzujący do autoryzacji tego bota na twój serwer.', inline = False)
    embed.add_field (name = 'd! happybirthday @user', value = 'Życzenie komuś wszystkiego najlepszego', inline = False)
    embed.add_field (name = 'd! technews', value = 'Użyj go, aby uzyskać nowości technologiczne', inline = False)
    embed.add_field (name = 'd! googlefy', value = 'Użyj go jak `` d! googlefy <string> ``.', inline = False)
    embed.add_field (name = 'd! spacenews', value = 'Użyj go, aby uzyskać wiadomości o spacji', inline = False)
    embed.add_field (name = 'd! phynews', value = 'Użyj go, aby uzyskać physycs', inline = False)
    embed.add_field (name = 'd! verify', value = 'Użyj go, aby uzyskać zweryfikowaną rolę. Uwaga - Wymaga właściwej konfiguracji.', inline = False)
    embed.add_field (name = 'd! flipcoin', value = 'Flipps coin', inline = False)
    embed.add_field (name = 'd! rolldice', value = 'Rolls dice', inline = False)
    embed.add_field (name = 'd! avatar @user', value = 'Pokazuje avatar', inline = False) 	
    poczekaj na client.send_message (autor, embed = embed)
    czekaj na client.say ('📨 Sprawdź DMs for Information')

@ client.command (pass_context = True)  
@ commands.has_permissions (kick_members = True)     
async def kick (ctx, użytkownik: discord.Member):

    jeśli user.server_permissions.kick_members:
        czekaj na client.say ('** On jest mod / admin i nie mogę go kopnąć **)
        powrót
    
    próbować:
        czekaj na client.kick (użytkownik)
        await client.say (user.name + 'został wyrzucony. Good bye' + user.name + '!')
        poczekaj na client.delete_message (ctx.message)

    z wyjątkiem niezgody. Zakazane:
        await client.say („Odmowa uprawnień”)
        powrót

@ client.command (pass_context = True)
@ commands.has_permissions (manage_messages = True)  
async def clear (ctx, number):
 
    jeśli ctx.message.author.server_permissions.manage_messages:
         mgs = [] # Pusta lista, aby umieścić wszystkie wiadomości w dzienniku
         liczba = int (liczba) # Konwersja ilości wiadomości do usunięcia na liczbę całkowitą
    async dla x w client.logs_from (ctx.message.channel, limit = liczba + 1):
        mgs.append (x)            
       
    próbować:
        poczekaj na client.delete_messages (mgs)          
        czekaj na klienta.say (str (numer) + „wiadomości usunięte”)
     
    z wyjątkiem niezgody. Zakazane:
        await client.say (embed = Forbidden)
        powrót
    z wyjątkiem discord.HTTPException:
        czekaj na client.say ('clear failed.')
        powrót         
   
 
    poczekaj na client.delete_messages (mgs)      



    	 		


@ client.command (pass_context = True)  
@ commands.has_permissions (ban_members = True)      
async def ban (ctx, użytkownik: discord.Member):

    jeśli user.server_permissions.ban_members:
        czekaj na client.say ('** On jest mod / admin i nie mogę go zablokować **')
        powrót

    próbować:
        czekaj na client.ban (użytkownik)
        await client.say (user.name + 'został zbanowany. Good bye' + user.name + '!')

    z wyjątkiem niezgody. Zakazane:

        await client.say („Odmowa uprawnień”)
        powrót
    z wyjątkiem discord.HTTPException:
        await client.say („błąd nie powiódł się”)
        powrót		 



@ client.command (pass_context = True)  
@ commands.has_permissions (ban_members = True)     


async def unban (ctx):
    ban_list = czekaj na client.get_bans (ctx.message.server)

    # Pokaż zablokowanych użytkowników
    await client.say ("Lista zakazów: n {}". format ("n" .join ([user.name dla użytkownika w ban_list])))

    # Odbanuj ostatniego zbanowanego użytkownika
    jeśli nie ban_list:
    	
        await client.say („Lista zakazów jest pusta”)
        powrót
    próbować:
        poczekaj na client.unban (ctx.message.server, ban_list [-1])
        await client.say ('Unbanned user: `{}`' .format (ban_list [-1] .name))
    z wyjątkiem niezgody. Zakazane:
        await client.say („Odmowa uprawnień”)
        powrót
    z wyjątkiem discord.HTTPException:
        poczekaj na klienta.say ('unban failed.')
        powrót		      	 		 		  
  
@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)
async def say (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)

    jeśli nie msg: await client.say („Proszę podać wiadomość do wysłania”)
    else: await client.say (msg)
    powrót

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def rules (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Określ użytkownika, który ma ostrzec”)
    inaczej: czekaj na client.say (msg + ', przeczytaj ponownie regulamin i nigdy więcej nie łam żadnego z nich, w przeciwnym razie wyciszę / kopnę / banuję następnym razem.))
    powrót

@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True) 
async def bans (ctx):
    '' 'Dostaje listę użytkowników, którzy już nas nie mają' ''
    x = czekaj na client.get_bans (ctx.message.server)
    x = 'n'.join ([y.name dla y in x])
    embed = discord.Embed (title = "List of the Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say (embed = embed)

@ client.command (pass_context = True)  
@ commands.has_permissions (kick_members = True)     

async def serverinfo (ctx):
    '' 'Wyświetla informacje o serwerze!' ''

    server = ctx.message.server
    role = [x.name dla x in server.role_hierarchy]
    role_length = len (role)

    jeśli role_length> 50: # W przypadku, gdy jest zbyt wiele ról ...
        role = role [: 50]
        roles.append ('>>>> Wyświetlanie [50 /% s] Ról'% len (role))

    role = ',' .join (role);
    channelz = len (server.channels);
    time = str (server.created_at); time = time.split (''); czas = czas [0];
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    join = discord.Embed (description = '% s'% (str (serwer)), title = 'Nazwa serwera', color = discord.Color ((r << 16) + (g << 8) + b)) ;
    join.set_thumbnail (url = server.icon_url);
    join.add_field (name = '__Owner__', value = str (server.owner) + 'n' + server.owner.id);
    join.add_field (name = '__ID__', value = str (server.id))
    join.add_field (name = '__Member Count__', value = str (server.member_count));
    join.add_field (name = '__Text / Voice Channels__', value = str (channelz));
    join.add_field (name = '__Roles (% s) __'% str (length_length), value = role);
    join.set_footer (text = 'Utworzono:% s'% time);

    return await client.say (embed = join);

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def norole (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Określ użytkownika, który ma ostrzec”)
    else: await client.say (msg + ', proszę nie pytać o zasady sprawdzania promocji ponownie.')
    powrót

@ client.command (pass_context = True)
async def happybirthday (ctx, *, msg = None):
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Określ użytkownika do życzenia”)
    oczekuj client.say ('Wszystkiego najlepszego' + msg + 'http: //asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    powrót

	
@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def english (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Określ użytkownika, który ma ostrzec”)
    else: await client.say (msg + ', proszę nie używać języka innego niż ** English. **')
    powrót

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True)
async def hindi (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Określ użytkownika, który ma ostrzec”)
    else: await client.say (msg + 'abe oo angrez ke bacche chup chap hindi me baat kar nahi to mai pagla jaunga')
    powrót


@ client.command (pass_context = True) 
async def htmltutorial (ctx, *, msg = None):
    poczekaj na client.delete_message (ctx.message)
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Proszę określić użytkownika”)
    inaczej: czekaj na client.say ('Welcome' + msg + ', sprawdź http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    powrót
   
@ client.command (pass_context = True)
async def github (ctx, *, msg = None):
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say ("Proszę określić respo.` `Format- https: // github.com / uksoftworld / DarkBot``"
    inaczej: czekaj na client.say ('https://github.com/' + msg)
    powrót

@ client.command (pass_context = True)
async def reactionroles (ctx, *, msg = None):
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: await client.say („Sprawdź ten film, aby skonfigurować YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ”)
    else: await client.say ('Sprawdź ten film, aby skonfigurować YAGPDB BOT- https://www.youtube.com/watch?v=icAqiw6txRQ' + msg)
    powrót

@ client.command (pass_context = True)
async def bottutorial (ctx, *, msg = None):
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    if not msg: await client.say ("Nie znaleziono samouczka lub błędnie go wpisałeś")
    inaczej: czekaj na client.say ('https://github.com/uksoftworld/discord.py-tutorial/blob/master/' + msg + '.py')
    powrót

@ client.command (pass_context = True)
async def dyno (ctx, *, msg = None):
    jeśli '@here' w msg lub '@everyone' w msg:
      powrót
    jeśli nie msg: czekaj na client.say ("Nie znaleziono nazwy polecenia lub błędnie ją wpisałeś")
    else: await client.say ('https://github.com/uksoftworld/dynoCC/blob/master/' + msg)
    powrót

@ client.command (pass_context = True)
async def unverify (ctx):
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Unverified')
    poczekaj na client.add_roles (ctx.message.author, role)
    
@ client.command (pass_context = True)
async def weryfikacja (ctx):
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Verified')
    poczekaj na client.add_roles (ctx.message.author, role)
    
@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)
async def friend (ctx, użytkownik: discord.Member,):
    poczekaj na client.delete_message (ctx.message)
    role = discord.utils.get (ctx.message.server.roles, name = 'Friend of Owner')
    poczekaj na client.add_roles (ctx.message.mentions [0], rola)

@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)     
async def makemod (ctx, użytkownik: discord.Member):
    nickname = '♏' + user.name
    czekaj na client.change_nickname (użytkownik, nick = nickname)
    role = discord.utils.get (ctx.message.server.roles, name = 'Moderator')
    czekaj na client.add_roles (użytkownik, rola)
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    embed = discord.Embed (color = discord.Color ((r << 16) + (g << 8) + b))
    embed.set_author (name = 'Congratulations Message')
    embed.add_field (name = '__Congratulations __', value = '** Gratulacje dla mod.Hope będziesz bardziej aktywny tutaj. Dziękujemy za pomoc i wsparcie. **', inline = False)
    embed.set_image (url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    czekaj na client.send_message (user, embed = embed)
    poczekaj na client.delete_message (ctx.message)
    
@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)     
async def removemod (ctx, użytkownik: discord.Member):
    nickname = user.name
    czekaj na client.change_nickname (użytkownik, nick = nickname)
    role = discord.utils.get (ctx.message.server.roles, name = 'Moderator')
    czekaj na client.remove_roles (użytkownik, rola)
    poczekaj na client.delete_message (ctx.message)

@ client.command (pass_context = True)
async def botwarncode (ctx):
    poczekaj na client.say („https://hastebin.com/ibogudoxot.py”)
    powrót

@ client.command (pass_context = True)
async def guess (ctx, number):
    próbować:
        arg = random.randint (1, 10)
    z wyjątkiem ValueError:
        czekaj na client.say („Nieprawidłowy numer”)
    jeszcze:
        await client.say ('Prawidłowa odpowiedź to' + str (arg))

@ client.command (pass_context = True)
@ commands.has_permissions (kick_members = True) 
asynchroniczne role def (kontekst):
	„” „Wyświetla wszystkie role z ich identyfikatorami” „”
	roles = context.message.server.roles
	result = "Role są"
	do roli w rolach:
		result + = '``' + rola.nazwa + '``' + ”:" + '``' + rola.id + '`' '+" n "
	czekaj na client.say (wynik)
    
@ client.command (pass_context = True, aliasy = ['serwer'])
@ commands.has_permissions (kick_members = True)
async def membercount (ctx, * args):
    „” „
    Pokazuje statystyki i informacje o aktualnej gildii.
    UWAGA: Używaj tego tylko na własnych gildiach lub z wyraźnymi
    uprawnienia administratorów gildii!
    „” „
    jeśli ctx.message.channel.is_private:
        czekaj na bot.delete_message (ctx.message)
        powrót

    g = ctx.message.server

    gid = g.id
    membs = str (len (g.members))
    membs_on = str (len ([m dla m in g.members, jeśli nie m.status == Status.offline]))
    users = str (len ([m dla m in g.members, jeśli nie m.bot])))
    users_on = str (len ([m dla m in g.members, jeśli nie m.bot, a nie m.status == Status.offline])))
    boty = str (len ([m dla m in g.members jeśli m.bot]))
    bots_on = str (len ([m dla m in g.members jeśli m.bot i nie m.status == Status.offline]))
    created = str (g.created_at)
    
    em = Osadź (title = „Membercount”)
    em.description = "` `` n "
                        „Członkowie:% s (% s) n”
                        „Użytkownicy:% s (% s) n”
                        „Boty:% s (% s) n”
                        „Utworzono:% s
                        „` `` ”% (membs, membs_on, users, users_on, bots, bots_on, created)

    poczekaj na client.send_message (ctx.message.channel, embed = em)
    poczekaj na client.delete_message (ctx.message)
	
@ client.command (pass_context = True)
@ commands.has_permissions (administrator = True)
async def embed (ctx, * args):
    „” „
    Wysyłanie osadzonych wiadomości z kolorem (a później tytuł, stopka i pola)
    „” „
    argstr = "" .join (args)
    r, g, b = krotka (int (x * 255) dla x w colorsys.hsv_to_rgb (random.random (), 1, 1))
    tekst = argument
    color = discord.Color ((r << 16) + (g << 8) + b)
    poczekaj na client.send_message (ctx.message.channel, embed = Embed (color = color, description = text))
    poczekaj na client.delete_message (ctx.message)


klient . run ( os . getenv ( „NjAwMDA5NTM3NDQ5MDk5MjY2.XSt6oA.wx8yZroB5QMiEKt2G0b-uupKYpc"))
