import React, {FC, Fragment} from "react";
import '@telegram-apps/telegram-ui/dist/styles.css';
import { Section, Cell, Image, List } from '@telegram-apps/telegram-ui';

import Page from '../../components/common/page.tsx';
import Link from '@/components/common/link.tsx';

const cellsTexts = ['Chat Settings', 'Data and Storage', 'Devices'];

const Index: FC = () => {
  return <Page back={false}>
    <List>
      {/* Section component to group items within the list */}
      <Section header="Header for the section" footer="Footer for the section">
        {/* Mapping through the cells data to render Cell components */}
        {cellsTexts.map((cellText, index) => (
          <Cell key={index}>
            {cellText}
          </Cell>
        ))}
      </Section>
    </List>
  </Page>
};

export default Index;