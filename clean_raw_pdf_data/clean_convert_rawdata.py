import pandas as pd
from PyPDF2 import PdfReader


def extract_pdf_text(filename):
    reader = PdfReader('RawData.pdf')  # create pdf reader object
    page = reader.pages[0]  # extract page
    text = page.extract_text()  # extract text
    rawdata = text.split('\n')[1:]  # cleaning
    rawdata = [i for i in rawdata if i != '#FEHLER!']
    return rawdata


def convert_text_to_lists(rawdata):
    counter = 0
    list_data = list()

    while counter < len(rawdata):
        try:
            # for rows that have complete information
            if '$' in rawdata[counter + 8]:
                list_data.append(rawdata[counter:counter + 9])
                counter += 9
            # These rows are missing domain information
            elif '$' in rawdata[counter + 7]:
                list_data.append(rawdata[counter:counter + 8])
                counter += 8
            # These rows are missing revenue information
            elif 'Hospitality' in rawdata[counter + 7]:
                list_data.append(rawdata[counter:counter + 8])
                counter += 8
            else:
                # These rows are missing both revenue and domain information
                list_data.append(rawdata[counter:counter + 7])
                counter += 7
        except IndexError:
            break

    return list_data


def convert_list_into_dataframe(list_data):
    first_name = list()
    last_name = list()
    title = list()
    country = list()
    domain = list()
    city = list()
    industry = list()
    revenue = list()
    company_name = list()
    company_size = list()
    not_arranged = list()

    # Sorting list_data into relevant column header list.
    for row in list_data:
        if len(row) == 9:
            first_name.append(row[0].split()[0])
            last_name.append(row[0].split()[1])
            title.append(row[1])
            country.append(row[2])
            domain.append(row[3])
            company_name.append(row[4])
            city.append(row[5])
            company_size.append(row[6])
            industry.append(row[7])
            revenue.append(row[8])
        elif len(row) == 8 and '@' not in row[3]:
            first_name.append(row[0].split()[0])
            last_name.append(row[0].split()[1])
            title.append(row[1])
            country.append(row[2])
            domain.append('N/A')
            company_name.append(row[3])
            city.append(row[4])
            company_size.append(row[5])
            industry.append(row[6])
            revenue.append(row[7])
        elif len(row) == 8 and '@' in row[3]:
            first_name.append(row[0].split()[0])
            last_name.append(row[0].split()[1])
            title.append(row[1])
            country.append(row[2])
            domain.append(row[3])
            company_name.append(row[4])
            city.append(row[5])
            company_size.append(row[6])
            industry.append(row[7])
            revenue.append('N/A')
        elif len(row) == 7:
            first_name.append(row[0].split()[0])
            last_name.append(row[0].split()[1])
            title.append(row[1])
            country.append(row[2])
            domain.append('N/A')
            company_name.append(row[3])
            city.append(row[4])
            company_size.append(row[5])
            industry.append(row[6])
            revenue.append('N/A')
        else:
            not_arranged.append(row)

    # Convert into dataframe
    df = pd.DataFrame(data={'First Name': first_name,
                            'Last Name': last_name,
                            'Title': title,
                            'Country': country,
                            'Domain': domain,
                            'City': city,
                            'Industry': industry,
                            'Revenue': revenue,
                            'Company Name': company_name,
                            'Company Size': company_size})

    return df


def convert_pdf_to_dataframe(filename):
    rawdata = extract_pdf_text(filename)
    list_data = convert_text_to_lists(rawdata)
    df = convert_list_into_dataframe(list_data)
    print(df)


if __name__ == '__main__':
    file_name = 'RawData.pdf'
    try:
        convert_pdf_to_dataframe(file_name)
    except:
        print('This file format is invalid for this cleaning script. Please provide a valid pdf file')

#%%
