<template>
    <div>
        <!-- <b-table stacked :items="items" thStyle="text-align: center"></b-table> -->
        <table>
            <tr>
                <div style="float: left; width: 50%;">
                    <th>Branch</th>
                    <td>{{ items[0].Branch }}</td>
                </div>
                <div style="float: left; width: 50%;">
                    <th>Tel</th>
                    <td>{{ items[0].Tel }}</td>
                </div>
            </tr>
            <br />
            <tr>
                <div style="float: left; width: 50%;">
                    <th>Area</th>
                    <td>{{ items[0].Area }}</td>
                </div>
                <div style="float: left; width: 50%;">
                    <th>Address</th>
                    <td>{{ items[0].Address }}</td>
                </div>
            </tr>
            <br />
        </table>
    </div>
</template>

<script>
export default {
    props: {
        items: {
            type: Array,
            default: function () {
                return [
                    {
                        Branch: null,
                        Area: null,
                        Tel: null,
                        Address: null,
                    },
                ]
            },
        },
    },
}
</script>

<style scoped>
table {
    margin: auto;
    width: 100%;
}
th{
    text-align: center;
    width: 70px;
}
td {
    padding-left: 30px;
}
</style>
