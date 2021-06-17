in_thread do
  use_synth :mod_pulse
  play 65
  play 69
  sleep 0.5
  play 65
  sleep 0.2
  play 63
  sleep 0.5
  play 65
  sleep 0.5
  play 65
  sleep 0.5
  play 65
  sleep 0.5
  play 60
  sleep 0.2
  play 65
end
in_thread do
  use_synth :saw
  sleep 2
  play 38
  sleep 0.25
  play 50
  sleep 0.25
  play 62
end
in_thread do
  play 99
  sleep 2
  play 99
  sleep 2
  play 99
  sleep 2
end

