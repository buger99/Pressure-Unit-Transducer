def pressure_converter(value, from_unit, to_unit):
    # 압력 단위 간의 변환 비율을 정의한 딕셔너리
    units = {
        "atm": 1.0,
        "Pa": 101325.0,
        "hPa": 1013.25,
        "kPa": 101.325,
        "MPa": 0.101325,
        "bar": 1.01325,
        "kg/cm2": 1.03323,
        "psi": 14.696,
        "mmHg": 760.0,
        "mmH2O": 10330.0
    }

    if from_unit in units and to_unit in units:
        # 변환 계산 수행
        result = value * units[from_unit] / units[to_unit]
        return result
    else:
        return "지원하지 않는 단위입니다."

# 메인 함수
def main():
    while True:
        try:
            value = float(input("압력 값을 입력하세요: "))
            from_unit = input("변환하려는 단위를 입력하세요 (atm, Pa, hPa, kPa, MPa, bar, kg/cm2, psi, mmHg, mmH2O): ")
            to_unit = input("변환하려는 대상 단위를 입력하세요 (atm, Pa, hPa, kPa, MPa, bar, kg/cm2, psi, mmHg, mmH2O): ")

            result = pressure_converter(value, from_unit, to_unit)
            if isinstance(result, float):
                print(f"{value} {from_unit}은(는) {result} {to_unit}입니다.")
            else:
                print(result)
        except ValueError:
            print("올바른 숫자를 입력하세요.")

        another_conversion = input("더 변환하시겠습니까? (yes/no): ")
        if another_conversion.lower() != "yes":
            break

# 프로그램 시작 지점
if __name__ == "__main__":
    main()
