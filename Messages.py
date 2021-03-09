m_start = 'Salam!\nMən Anonim Çhat Botuyam\nMənim Sayəmdə Telegramda Bota qoşulan hərhansı biri ilə Anonim söhbət edə bilər və əgər söhbətiniz tutarsa 2 tərəf Like etdikdə Siz şəxsi söhbətə yönləndiriləcəksiniz\nƏgər söhbətiniz Tutmazsa Dislike edərək digər söhbətə keçə bilərsiniz.\nDİQQƏT! Botun uğurlu işləməsi üçün istifadəçi adınız olmalıdır, parametirləri yoxlayın və istifadəçi adı qoyduğunuzdan əmin olun\nBotu dayandırmaq üçün /stop yazın. Unutmayın ki bütün məlumatlarınız silinəcək, əks halda məlumatlarınız data bazada qalacaq. '

m_is_not_free_users = 'Üzür istəyirəm amma hazırda botda heçkim yoxdu\nBota qatılan olarsa sizinlə söhbətə birləşdiriləcək'
m_is_connect = 'Əlaqə Quruldu! Həmsöhbətə salam göndərin!'

m_play_again = 'Başqası ilə söhbət etmək istəyirsiniz?'

m_is_not_user_name = 'Bağışlayın, ancaq botumuzda yalnız bir istifadəçi adınız olduğu halda əlaqə qurmaq mümkündür'

m_good_bye = 'Bot: Əlvida, səni yenidən görməkdən məmnun qalacağıq!'

m_disconnect_user = 'Bot: Həmsöhbətiniz əlaqəni kəsdi'

m_failed = 'Bot: Bir səhv baş verdi!'

m_like = 'Bot: əla seçimdir!'

m_dislike_user = 'Bot: Dialoq sona çatdı'

m_dislike_user_to = 'Bot: Həmsöhbət sizi bəyənmədi, bağışlayın'

m_send_some_messages = 'Bot: öz mesajlarınızı yönləndirə bilməzsiniz'

m_has_not_dialog = 'Dialoqdasınız'

dislike_str = '\U0001F44E Bəyənmirəm'

like_str = '\U0001F44D Bəyənirəm'


def m_all_like(x):
    return 'Həmsöhbət səni bəyəndi\n' + 'İstifadəçi adı: @' + str(x) + \
           '\nÜnsiyyətinizdə uğurlar.!\nBizimlə olduğunuz üçün təşəkkür edirik!'
