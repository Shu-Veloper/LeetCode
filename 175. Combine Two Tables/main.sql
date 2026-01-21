SELECT p.firstName,p.lastName,a.city,a.state
FROM Person p
-- Personの値を基準にしてAddressと結合
-- LEFT JOINは 基準のテーブルに対応する行がAddressに存在しない場合でも、基準のテーブルの行を結果に含める
LEFT JOIN Address a
    ON p.personId = a.personId