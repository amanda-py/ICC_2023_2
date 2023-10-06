h_i, m_i, h_f, m_f = map(int, input().split())


if h_i >= h_f:
    h_f += 24

if (m_f - m_i)< 0:
    h_f-= 1
    duracao_minutos = 60 - abs(m_f - m_i)
    
else:
    duracao_minutos = m_f - m_i


duracao_horas = h_f - h_i

print(f'O jogo durou {duracao_horas} hora(s) e {duracao_minutos} minuto(s).')