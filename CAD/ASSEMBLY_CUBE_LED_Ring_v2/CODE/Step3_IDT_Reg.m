%% Repeat IDT algorithm

Normalized_term=(sum_PTF+Alpha).*(sum_ATF+Beta)-conj_term1.*conj_term2;
V_re = ((sum_ATF+Beta).* conj_PTF_Iten - conj_term1.* conj_ATF_Iten) ./ Normalized_term;
V_im = ((sum_PTF+Alpha).* conj_ATF_Iten - conj_term2.* conj_PTF_Iten) ./ Normalized_term;

disp('Performing IDT spends...');
toc

v_im = real(ifft2((V_im)));
v_re = real(ifft2((V_re)));

n_re = sqrt(((n_Medium.^2 + v_re) + sqrt((n_Medium^2 + v_re).^2 + v_im.^2)) / 2);
n_im = v_im ./ n_re ./ 2;

RI=n_re+1i*n_im;

